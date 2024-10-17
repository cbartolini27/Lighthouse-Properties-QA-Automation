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
        logger.info(f"*********Cookies successfully rejected*********")
        assert True, "Cookies successfully rejected"
    else:
        logger.info(f"*********Cookies not successfully rejected*********")
        assert False, "Cookies not successfully rejected"
    