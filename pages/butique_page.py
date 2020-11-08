from selenium.webdriver import ActionChains
import logging
from utils.locators import *
from utils.users import Users
import time


class ButiquePage():


    def __init__(self,driver):
        self.driver = driver
        self.choosedStore = Locators.choosedStore
        self.choosedProduct = Locators.chooseProduct
        self.addToBasketButton = Locators.addToBasketButton



    def selectStore(self):
        driver = self.driver
        driver.find_element(*self.choosedStore).click()

    def isProductPageVisible(self):
        driver = self.driver
        try:
            driver.find_element(*self.addToBasketButton)
            logging.info("Product page is visible.")
            return True
        except:
            logging.warning("Product Page Error")
            return False


    def checkProductImagesInStore(self):
        driver = self.driver
        time.sleep(1)
        productCount = len(driver.find_elements_by_class_name("boutique-product"))
        print("Bu sayfada" + str(productCount) + "ürün bulunmaktadır.")



        for x in range(1,productCount):
            try:
                elementPath = "div.boutique-product:nth-child(" + str(x) + ") > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
                mainElem = driver.find_element_by_css_selector(elementPath)
                mainElemSrc = driver.find_element_by_css_selector(elementPath).get_attribute("src")
                driver.execute_script("arguments[0].scrollIntoView();", mainElem)
                print(elementPath)
                print(mainElemSrc)

                ###Get Element attributes
                productPath = "div.boutique - product: nth - child(" + str(x) + ")"
                productTitle = driver.find_element_by_css_selector(productPath).get_attribute("title")
                productID = driver.find_element_by_css_selector(productPath).get_attribute("id")

                if(mainElemSrc == "/Content/images/defaultThumb.jpg"):
                    logging.error("Fotoğraf yüklenemedi. ProductID : " + productID + "Product Title : " + productTitle )
                else:
                    logging.info("Fotoğraf başarıyla görüntülendi. Product ID : " + productID + "Product Title : " + productTitle)

            except Exception:
                pass



    def selectProduct(self):
        driver = self.driver
        product = driver.find_element(*self.choosedProduct)
        driver.execute_script("arguments[0].scrollIntoView();", product)
        product.click()



