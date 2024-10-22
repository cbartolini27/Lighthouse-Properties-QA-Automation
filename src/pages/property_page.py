from selenium.webdriver.common.by import By
from src.elements import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import locator

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class PropertyPage(BasePage):
    '''
    Viewing property
    '''
    def click_first_property(self):
        first_property = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.PropertyPageLocators.PROPERTY_CARDS)
        )
        first_property.click()   
        
    def click_left_button(self):
        left_arrow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.PropertyPageLocators.LEFT_IMAGE_ARROW)
        )
        left_arrow.click()     
        
    def click_right_button(self):
        right_arrow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.PropertyPageLocators.RIGHT_IMAGE_ARROW)
        )
        right_arrow.click()     
    
    def get_num_property_images(self):
        pictures = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator.PropertyPageLocators.PROPERTY_IMAGES)
        )
        return len(pictures)
    
    def get_selected_img(self):
        selected_img = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.PropertyPageLocators.SELECTED_PROPERTY_IMAGE)
        )
        get_img = selected_img.find_element(By.TAG_NAME, 'img')

        get_src = get_img.get_attribute('src')
        return get_src
    
        