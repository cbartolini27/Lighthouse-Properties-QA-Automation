from selenium.webdriver.common.by import By

class MainPageLocators(object):
    AGREE_COOKIE_BUTTON = ('xpath', "//button[contains(@class, 'cookie-button-text') and text()='Piekrītu']")
    REJECT_COOKIE_BUTTON = ('xpath', "//button[contains(@class, 'cookie-button-text') and text()='Noraidīt']")

#Each class represents a new pages locators. Whatever search result is here add new locators