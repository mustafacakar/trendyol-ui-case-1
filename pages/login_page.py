from selenium.webdriver import ActionChains

from utils.locators import *
from utils.users import Users
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.emailTextbox = Locators.emailTextbox
        self.passTextbox = Locators.passwordTextbox
        self.loginButton = Locators.loginButton
        self.testMail = Users.TEST_USER1
        self.testPass = Users.TEST_PASS1

    def user_login(self):
        driver = self.driver
        driver.find_element(*self.emailTextbox).send_keys(*self.testMail)
        driver.find_element(*self.passTextbox).send_keys(*self.testPass)
        driver.find_element(*self.loginButton).click()
