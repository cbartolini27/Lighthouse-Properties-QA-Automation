from selenium.webdriver.common.by import By

class MainPageLocators(object):
    AGREE_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Piekrītu']]")
    REJECT_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Noraidīt']]")

#Each class represents a new pages locators. Whatever search result is here add new locators