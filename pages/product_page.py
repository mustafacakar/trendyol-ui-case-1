from selenium.webdriver import ActionChains

from utils.locators import *
from utils.users import Users



class ProductPage():

    def __init__(self,driver):
        self.driver = driver
        self.addToBasketButton = Locators.addToBasketButton


    def addToBasket(self):
        driver = self.driver
        driver.find_element(*self.addToBasketButton).click()