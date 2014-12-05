__author__ = 'avasilyev2'

from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class LoginPage(BasePage):

    def is_title_matches(self):
        return "UKR" in self.driver.title

    def login_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.NAME, 'Login')))

    def password_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.NAME, 'Password')))

    def login_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    def error_message(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='error-text']")))

    def login_username(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='username']")))

    def logout_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='logout']")))

    def login(self, name, password):
        self.login_field().send_keys(name)
        self.password_field().send_keys(password)
        self.login_button().click()