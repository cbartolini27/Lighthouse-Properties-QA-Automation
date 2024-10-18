import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.main_page import MainPage
from utilities.logger import Log_maker


#Instance of global log
logger = Log_maker.log_gen()

@pytest.fixture
def driver(): 

    logger.info("*********Setting up WebDriver*********")
    service = Service(executable_path=r"C:\Users\Christian Bartolini\Desktop\Selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.lighthouseproperties.lv/")
    
    logger.info("*********Navigated to https://www.lighthouseproperties.lv/*********")
    yield driver
    
    driver.quit()

def test_agree_button_cookies(driver):
    main_page = MainPage(driver)
    main_page.click_agree_cookie()
    logger.info("*********Agree button successfully clicked*********")
    
    #Need to refresh driver to allow cookies to come in
    driver.refresh()
   
    cookies = driver.get_cookies()  # This returns a list of dictionaries, each representing a cookie
    logger.info(f"*********Cookies retrieved: {cookies}*********")
    logger.info(f"*********Length of cookie string: {len(cookies)}*********")
    
    assert any(cookie['name'] == 'ga-disable' and cookie['value'] == 'false' for cookie in cookies), "Cookie 'ga-disable' not set correctly"
    logger.info("*********'ga-disable' cookie is set correctly!*********")

    # Assert for another specific cookie if needed
    assert any(cookie['name'] == 'localConsent' and cookie['value'] == 'true' for cookie in cookies), "Cookie 'localConsent' not set correctly"
    logger.info("*********'localConsent' cookie is set correctly!*********")

def test_reject_button_cookies(driver):
    main_page = MainPage(driver)
    main_page.click_reject_cookie()
    logger.info("*********Reject button successfully clicked*********")
    
    #Need to refresh driver to allow cookies to come in
    driver.refresh()
   
    cookies = driver.get_cookies()  # This returns a list of dictionaries, each representing a cookie
    logger.info(f"*********Cookies retrieved: {cookies}*********")
    logger.info(f"*********Length of cookie string: {len(cookies)}*********")
    
    if len(cookies) == 0:
        logger.info("*********Cookies successfully rejected*********")
        assert True, "Cookies successfully rejected"
    else:
        logger.info("*********Cookies not successfully rejected*********")
        assert False, "Cookies not successfully rejected"


@pytest.mark.parametrize("click_method, link_text", [
    ('click_privacy_policy', 'privātuma politiku'),
    ('click_privacy_policy_second', 'Lasīt privātuma politiku')
])
def test_privacy_policy_page(driver, click_method, link_text):
    mainPage = MainPage(driver)
    time.sleep(3)
   
    #Dynamically call the click_method
    getattr(mainPage, click_method)()
    logger.info(f"*********{click_method} successfully clicked: {link_text}*********")
    
    time.sleep(3)
    if mainPage.privacy_policy_heading_matches():
        logger.info("*********Successfully opened privacy policy page*********")
        assert True, "Successfully opened privacy policy page"
    else: 
        logger.info("*********Privacy policy page did not open successfully*********")
        assert False, "Privacy policy page did not open successfully"
  
def test_to_seller_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()
    
    if mainPage.click_to_the_seller_link():
        logger.info("*********Successfully opened seller page*********")
        assert True, "Successfully opened privacy seller page"
    else:
        logger.info("*********Seller page did not open successfully*********")
        assert False, "Seller page did not open successfully"
  
def test_to_buyer_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()
    
    if mainPage.click_to_the_buyer_link():
        logger.info("*********Successfully opened buyer page*********")
        assert True, "Successfully opened privacy buyer page"
    else:
        logger.info("*********Buyer page did not open successfully*********")
        assert False, "Buyer page did not open successfully"
  
def test_about_us_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()

    time.sleep(5)
    if mainPage.click_to_about_us_link:
        logger.info("*********Successfully opened about us page*********")
        assert True, "Successfully opened about us page"
    else:
        logger.info("*********About us page did not open successfully*********")
        assert False, "About us page did not open successfully"


def test_properties_load(driver):
    mainPage = MainPage(driver)
    min_per_page = 1
    max_per_page = 6
    mainPage.click_agree_cookie()
    
    total_pages = mainPage.get_property_page_count() 
    
    #Forward navigation check
    logger.info("*********Forward navigation check*********")
    for i in range(0, total_pages):
        number_of_properties = mainPage.count_property_cards() 
        
        if  number_of_properties >= min_per_page and number_of_properties <= max_per_page: 
            logger.info(f"*********Page {i + 1} has the correct number of properties = {number_of_properties}*********")
            assert True
        elif number_of_properties > max_per_page:
            logger.info(f"*********Page {i + 1} has too many properties = {number_of_properties}*********")
            assert False, f"Too many properties on page {i + 1}: {number_of_properties}"
        elif number_of_properties < min_per_page:
            logger.info(f"*********Page {i + 1} has too few properties = {number_of_properties}*********")
            assert False, f"Too few properties on page {i + 1}: {number_of_properties}"
        
        #- 1 to total pages because we dont want to click past the last page
        if i < total_pages - 1:
            mainPage.click_next_property_page()
       
    logger.info("*********Forward navigation passed*********")
    
    #Begin backward navigation
    logger.info("*********Beginning backward navigation*********")
    for i in range(total_pages -1, -1, -1):
        number_of_properties = mainPage.count_property_cards()  # Get number of properties on the current page

        if min_per_page <= number_of_properties <= max_per_page:
            logger.info(f"*********Page {i + 1} has the correct number of properties = {number_of_properties}*********")
            assert True
        elif number_of_properties > max_per_page:
            logger.info(f"*********Page {i + 1} has too many properties = {number_of_properties}*********")
            assert False, f"Too many properties on page {i + 1}: {number_of_properties}"
        elif number_of_properties < min_per_page:
            logger.info(f"*********Page {i + 1} has too few properties = {number_of_properties}*********")
            assert False, f"Too few properties on page {i + 1}: {number_of_properties}"

        # Don't click previous arrow on the first page
        if i > 0:
            mainPage.click_previous_property_page()
    logger.info("*********Backward navigation passed*********")