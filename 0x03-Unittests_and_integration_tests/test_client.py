#!/usr/bin/env python3

"""Unittest for utils.py
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url
        """
        test_url = "https://api.github.com/orgs/google/repos"
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            test_class = GithubOrgClient("google")
            self.assertEqual(test_class._public_repos_url, test_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos
        """
        test_url = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [{"name": "google"}, {"name": "abc"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            test_class = GithubOrgClient("google")
            self.assertEqual(test_class.public_repos(), ["google", "abc"])
            mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license
        """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.has_license(repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass method
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tearDownClass method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos
        """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), [])
        self.get_patcher.stop()

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license
        """
        test_class = GithubOrgClient("google")
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://google.com"}
            with patch('client.GithubOrgClient.public_repos') as mock_public:
                mock_public.return_value = [
                    {"name": "google", "license": {"key": "my_license"}}]
                self.assertEqual(test_class.public_repos("my_license"),
                                 ["google"])
                mock_public.assert_called_once_with("my_license")
