from selenium.webdriver.common.by import By
from src.elements import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import locator


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    
    #Extension of basepage, Returns true if PRIVĀTUMA POLITIKA is in webpage
    def privacy_policy_heading_matches(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'privacy-policy-description-heading'))
        )
        return "PRIVĀTUMA POLITIKA" in element.text
    
    def click_agree_cookie(self):
        # Wait until the button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.AGREE_COOKIE_BUTTON)
        )
        
        element = self.driver.find_element(*locator.MainPageLocators.AGREE_COOKIE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)  # Use JavaScript to click
    
    def click_reject_cookie(self): 
        # Wait until the button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.REJECT_COOKIE_BUTTON)
        )
     
        element = self.driver.find_element(*locator.MainPageLocators.REJECT_COOKIE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
    
    def click_privacy_policy(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.PRIVACY_POLICY_LINK)
        )
        
        element = self.driver.find_element(*locator.MainPageLocators.PRIVACY_POLICY_LINK)
        self.driver.execute_script("arguments[0].click();", element)
