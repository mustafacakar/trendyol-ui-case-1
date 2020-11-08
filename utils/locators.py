from selenium.webdriver.common.by import By

class Locators():


    ## Global Variables

    baseURL = "https://trendyol.com"



    ## Homepage Locators

    accountButton = (By.ID , "accountBtn")
    accountLoginButton = (By.CSS_SELECTOR,"div.account-button:nth-child(1)")
   # popupCloseButton = (By.XPATH,"/html/body/div[8]/div/div/a") çalışıyodu
    popupCloseButton = (By.CSS_SELECTOR,"html.fancybox-margin.fancybox-lock body div.fancybox-overlay.fancybox-overlay-fixed div.fancybox-wrap.fancybox-desktop.fancybox-type-html.fancybox-opened div.fancybox-skin a.fancybox-item.fancybox-close")



    # LoginPage Locators

    emailTextbox = (By.ID, "login-email")
    passwordTextbox = (By.ID,"login-password-input")
    loginButton = (By.CSS_SELECTOR,".q-primary")


    # ButiquePage Locators

    firstButique = (By.CSS_SELECTOR,"#navigation-wrapper > nav > ul > li:nth-child(1)")
    choosedStore = (By.CSS_SELECTOR, "#browsing-gw-homepage > div > div:nth-child(2) > div.sticky-wrapper > div.component-list.component-big-list > article:nth-child(1)")
    chooseProduct = (By.CSS_SELECTOR, "#boutique-detail-app > div > div:nth-child(2) > div > div:nth-child(1)")
    addToBasketButton = (By.CSS_SELECTOR,".add-to-bs")