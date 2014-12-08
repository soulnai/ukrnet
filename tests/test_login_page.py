from pageObjects.login_page import LoginPage

__author__ = 'avasilyev2'

from pageObjects.login_page import LoginPage
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login = "automation.tc@ukr.net"
password = "ololobumbum"
checkin = False

selenium_grid_url = 'http://172.23.62.121:4444/wd/hub'
chrome_driver = webdriver.Remote(selenium_grid_url, desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True})
firefox_driver = webdriver.Remote(selenium_grid_url, desired_capabilities={'platform': 'ANY', 'browserName': 'firefox', 'version': '', 'javascriptEnabled': True})



#def setUp():

  #login_page = LoginPage(driver)

    #def tearDown(self):
        #self.driver.quit()
     #   pass


@pytest.mark.parametrize('driver', [chrome_driver, firefox_driver])
def test_login_with_wrong_credentials(driver):
    login_page = LoginPage(driver)
    driver.get("http://www.ukr.net")
    login_page.login("name", "pasword")
    assert login_page.error_message().is_displayed() is True
    #unittest.TestCase.assertEqual(login_page.error_message().is_displayed(), True, "Should return error-message")

@pytest.mark.parametrize('driver', [chrome_driver, firefox_driver])
def test_login_with_credentials_in_all_uppercase(driver):
    login_page = LoginPage(driver)
    driver.get("http://www.ukr.net")
    login_page.login(login.upper(), password.upper())
    assert login_page.error_message().is_displayed() is True
    #unittest.TestCase.assertEqual(login_page.error_message().is_displayed(), True, "Should return error-message")


@pytest.mark.run('first')
@pytest.mark.parametrize('driver', [chrome_driver, firefox_driver])
def test_login(driver):
    login_page = LoginPage(driver)
    driver.get("http://www.ukr.net")
    login_page.login(login, password)
    global checkin
    checkin = True
    assert login_page.login_username().is_displayed() is True
    #unittest.assertEqual(login_page.login_username().is_displayed(), True, "Login should be successfull")
    login_page.logout_button().click()

@pytest.mark.run(after='first')
@pytest.mark.skipif("checkin is False")
@pytest.mark.parametrize('driver', [chrome_driver, firefox_driver])
def test_logout(driver):
        login_page = LoginPage(driver)
        driver.get("http://www.ukr.net")
        login_page.login(login, password)
        login_page.logout_button().click()
        assert login_page.login_button().is_displayed() is True
        #unittest.assertEqual(login_page.login_button().is_displayed(), True, "Logout should be performed correct")
