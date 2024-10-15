import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
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

def test_agree_button(driver):
    main_page = MainPage(driver)
    main_page.click_agree_cookie
    logger.info("*********Agree button successfully clicked*********")
   
    assert True
    
