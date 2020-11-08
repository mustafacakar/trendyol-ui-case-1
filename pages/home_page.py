import time

from selenium.webdriver import ActionChains
import logging
from utils.locators import *
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class Homepage(BasePage):


    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver
        self.popupClose = Locators.popupCloseButton
        self.accountButton = Locators.accountButton
        self.accloginButton = Locators.accountLoginButton
        self.firstButique = Locators.firstButique
        self.emailTextbox = Locators.emailTextbox
        self.loginButton = Locators.loginButton

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()


    def openHomePage(self):
        driver = self.driver
        driver.get("https://trendyol.com")
        try:
            driver.find_element(*self.popupClose).click()
            print("Gender popup closed.")
        except:
            print("Gender Popup aldready closed.")
        assert "Trend" in driver.title



    def clickLoginButton(self):
        driver = self.driver
        self.hover(*self.accountButton)
        driver.find_element(*self.accloginButton).click()
        self.is_element_present(*self.emailTextbox)

    def isLoginPageVisible(self):
        driver = self.driver
        try:
         self.driver.find_element(*self.loginButton)
         logging.info("Login Page Loaded Succesfully")
         return True
        except:
            logging.warning("Login Page Error.")
            return False

    def isHomepageVisible(self):
        driver = self.driver
        try:
            self.driver.find_element(*self.firstButique)
            logging.info("Home Page Loaded successfully")
            return True
        except:
            logging.warning("Home Page Load Error")
            return False



    def checkButiqueImages(self):
        driver = self.driver
        driver.find_element(*self.firstButique).click()

        ## turn all categories
        for x in range(1,9):
            butiqueElement = "#navigation-wrapper > nav > ul > li:nth-child(" + str(x) + ")"
            driver.find_element_by_css_selector(butiqueElement).click()
            butiqueCount = len(driver.find_elements_by_class_name("component-item"))

            # ## turn images in one butique
            for y in range(1,butiqueCount):
                time.sleep(0.25)
                imgPath = "article.component-item:nth-child(" + str(y) + ") > a:nth-child(1) > span:nth-child(1) > img:nth-child(1)"

                imgElement = driver.find_element_by_css_selector(imgPath)
                imgSrc = driver.find_element_by_css_selector(imgPath).get_attribute("src")
                driver.execute_script("arguments[0].scrollIntoView();", imgElement)

                ## If image is not load -> https://cdn.dsmcdn.com//web/production/large_boutique_placeholder.png
                ## setting placeholoder url for image src.
                if(imgSrc != "https://cdn.dsmcdn.com//web/production/large_boutique_placeholder.png"):
                    logging.info("Image Başarıyla yüklendi. Başarılı URL : " + imgSrc)
                else:
                    logging.warning("Image Başarısız Yüklendi. Başarısız URL : " + imgSrc)




