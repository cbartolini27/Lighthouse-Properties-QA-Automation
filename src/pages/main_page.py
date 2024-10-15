from selenium.webdriver.common.by import By
from src.elements import BasePageElement
from src import locator

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    
    def is_title_matches(self):
        return "Lighthouse Properties nekustamo īpašumu aģentūra" in self.driver.title
    
    def click_agree_cookie(self): 
        element = self.driver.find_element(*locator.MainPageLocators.AGREE_COOKIE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        return 
    
    def click_reject_cookie(self): 
        element = self.driver.find_element(*locator.MainPageLocators.REJECT_COOKIE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)