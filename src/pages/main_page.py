from selenium.webdriver.common.by import By
from src.elements import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src import locator




class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    '''
    Inital Prompts - ADD REASON FOR THESE
    '''
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
    
    def click_privacy_policy_second(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.PRIVACY_POLICY_LINK_SECOND)
        )
        
        element = self.driver.find_element(*locator.MainPageLocators.PRIVACY_POLICY_LINK_SECOND)
        self.driver.execute_script("arguments[0].click();", element)
    
    def privacy_policy_heading_matches(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'privacy-policy-description-heading'))
        )
        return "PRIVĀTUMA POLITIKA" in element.text
    
    '''
    Navigation bar features - ADD REASON FOR THESE
    '''
    def click_home_page(self):
        home_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.MainPageLocators.HOME_PAGE_BUTTON)
        )
        home_button.click()
        
        home_page = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "property-list-header"))
        )
        return "Īpašumi pārdošanā" in home_page.text
        
    def click_to_the_seller_link(self):
        seller_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.MainPageLocators.TO_THE_SELLER_LINK)
        )
        seller_link.click() 
        
        selling_plan_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "selling-plan-heading"))
        )
        return "Nekustamā īpašuma pārdošanas plāns" in selling_plan_element.text 
    
    def click_to_the_buyer_link(self):
         buyer_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.MainPageLocators.TO_THE_BUYER_LINK)
        )
         buyer_link.click() 
        
         property_list_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "property-list-header"))
        )
         return "Īpašumi pārdošanā" in property_list_header.text 
    
    def click_to_about_us_link(self):
         about_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.MainPageLocators.ABOUT_US_LINK)
        )
         about_link.click() 
        
         about_list_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "about-intro-heading"))
        )
         return "Mūsu filozofija" in about_list_header.text 
    
    
    '''
    Property filter section - ADD REASON FOR THESE 
    '''
    def click_next_property_page(self):
        arrow_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.NEXT_PROPERTY_PAGE_BUTTON)
        )
        arrow_button.click()
    
    def click_previous_property_page(self):
        arrow_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.PREVIOUS_PROPERTY_PAGE_BUTTON)
        )
        arrow_button.click()
    
    #Gets the number of properties on the current page
    def count_property_cards(self):
        property_cards = WebDriverWait(self.driver, 10).until(
            #Visibility_of_all_elements returns a list of all elements with locator strategy and locator value
            EC.visibility_of_all_elements_located(locator.MainPageLocators.PROPERTY_CARDS) 
        )

        return len(property_cards)
    
    #Counts how many pages there are for the property page
    def get_property_page_count(self):
        page_count_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator.MainPageLocators.PROPERTY_PAGE_COUNT_TEXT)
        ).text
       
        # page_count_text text format example, its in Latvian: (lapa1no3) 
        total_pages = page_count_text.split("no")[1].strip().replace(")", "") #split method splits into a list of substrings, [1] gets '3)', strip removes all white spaces, replace(), removes all instances of ')' with another string, in this case ""
        return int(total_pages)
    
    def click_property_type_privatmajas(self):
        privatmajas_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.PRIVATMAJAS_BUTTON)
        )
        privatmajas_button.click()
 
    def click_property_type_dzivokli(self):
        dzivokli_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.DZIVOKLI_BUTTON)
        )
        dzivokli_button.click()
   
    def click_property_type_komercipasumi(self):
        komercipasumi_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.KOMERCIPASUMI_BUTTON)
        )
        komercipasumi_button.click()
    
    def click_property_type_zemes(self):
        zemes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.MainPageLocators.ZEMES_BUTTON)
        )
        zemes_button.click()     
    