
from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.butique_page import ButiquePage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from utils.locators import Locators
from selenium import webdriver
import unittest
from utils.testCases import test_cases


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls,browser="firefox"):
        if(browser == "chrome"):
            cls.driver = webdriver.Chrome()
        elif(browser == "ie"):
            cls.driver = webdriver.Ie()
        elif(browser == "safari"):
            cls.driver = webdriver.Safari()
        else :
            cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_1_homepage_load(self):
        print("\n" + str(test_cases(0)))
        driver = self.driver
        page = Homepage(driver)
        page.openHomePage()
        assert "Trend" in driver.title

    def test_2_login_page_load(self):
        print("\n" + str(test_cases(1)))
        driver = self.driver
        page = Homepage(driver)
        page.clickLoginButton()
        assert "/giris" in driver.current_url
        self.assertTrue(page.isLoginPageVisible())


    def test_3_valid_user_login(self):
        print("\n" + str(test_cases(2)))
        driver = self.driver
        page = LoginPage(driver)
        page.user_login()


    def test_4_check_butique_images(self):
        print("\n" + str(test_cases(3)))
        driver = self.driver
        page = Homepage(driver)
        page.checkButiqueImages()

    def test_5_check_images_in_selected_store(self):
        print("\n" + str(test_cases(4)))
        driver = self.driver
        page =  ButiquePage(driver)
        page.selectStore()
        page.checkProductImagesInStore()

    def test_6_select_product(self):
        print("\n" + str(test_cases(5)))
        driver = self.driver
        page = ButiquePage(driver)
        page.selectProduct()
        self.assertTrue(page.isProductPageVisible())

    def test_7_add_to_basket(self):
        print("\n" + str(test_cases(6)))
        driver = self.driver
        page = ProductPage(driver)
        page.addToBasket()

    def test_finish(self):
            self.driver.close()
