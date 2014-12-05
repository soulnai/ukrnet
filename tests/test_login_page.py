__author__ = 'avasilyev2'

from pageObjects import login_page
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login = "automation.tc@ukr.net"
password = "ololobumbum"


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.ukr.net")
        self.login_page = login_page.LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_wrong_credentials(self):
        self.login_page.login("name", "pasword")
        self.assertEqual(self.login_page.error_message().is_displayed(), True, "Should return error-message")

    def test_login_with_credentials_in_all_uppercase(self):
        self.login_page.login(login.upper(), password.upper())
        self.assertEqual(self.login_page.error_message().is_displayed(), True, "Should return error-message")

    def test_login(self):
        self.login_page.login(login, password)
        self.assertEqual(self.login_page.login_username().is_displayed(), True, "Login should be successfull")

    def test_logout(self):
        if self.login_page.login(login, password):
            self.login_page.logout_button().click()
            self.assertEqual(self.login_page.login_button().is_displayed(), True, "Logout should be performed correct")
