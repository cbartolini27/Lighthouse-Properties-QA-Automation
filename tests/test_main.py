import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.main_page import MainPage
from src.pages.property_page import PropertyPage
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

def test_home_button(driver):
    main_page = MainPage(driver)
    main_page.click_agree_cookie()
    main_page.click_to_about_us_link()
    

    if main_page.click_home_page():
        logger.info("*********Successfully navigated to home page*********")
        assert True
    else: 
        logger.info("*********Navigation to home page unsuccessful*********")
        assert False, "Navigation to home page unsuccessful"
    
def test_to_seller_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()
    
    if mainPage.click_to_the_seller_link():
        logger.info("*********Successfully opened seller page*********")
        assert True
    else:
        logger.info("*********Seller page did not open successfully*********")
        assert False, "Seller page did not open successfully"
  
def test_to_buyer_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()
    
    if mainPage.click_to_the_buyer_link():
        logger.info("*********Successfully opened buyer page*********")
        assert True
    else:
        logger.info("*********Buyer page did not open successfully*********")
        assert False, "Buyer page did not open successfully"
  
def test_about_us_link(driver):
    mainPage = MainPage(driver)
    mainPage.click_agree_cookie()

    
    if mainPage.click_to_about_us_link:
        logger.info("*********Successfully opened about us page*********")
        assert True
    else:
        logger.info("*********About us page did not open successfully*********")
        assert False, "About us page did not open successfully"


@pytest.mark.parametrize("click_method, property_type", [
    ('click_property_type_privatmajas','Privātmājas'),
    ('click_property_type_dzivokli','Dzīvokļi'),
    ('click_property_type_komercipasumi','Komercīpašumi'),
    ('click_property_type_zemes','Zemes')
])
def test_properties_load(driver, click_method, property_type):
    mainPage = MainPage(driver)
    min_per_page = 1
    max_per_page = 6
    mainPage.click_agree_cookie()
    
    #Allows for different property types to get tested
    getattr(mainPage, click_method)()
    logger.info(f"*********{click_method} successfully clicked: {property_type}*********")
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

def test_img_duplicates(driver):
    main_page = MainPage(driver)
    property_page = PropertyPage(driver)
    main_page.click_agree_cookie()
    property_page.click_first_property()
    
    num_images = property_page.get_num_property_images()
    logger.info(f"*********Number of property images: {num_images}*********")
     
    #Getting the src info of each image then storing into a list
    src_li = []
    for img in range(num_images):
        img_src = property_page.get_selected_img()
        src_li.append(img_src)
        
        if (img + 1) != num_images:
            property_page.click_right_button()

    logger.info(f"*********Src for each img: {src_li}*********")
    
    #Checking for duplicate images using their src info previously stored in src_li list. Using set b/c O(1) and allows no duplicates
    seen = set()
    for src in src_li:
        if src not in seen:
            seen.add(src)
        else:
            logger.info(f"*********You have duplicate images for img: {src}*********")
            assert False, 'You have duplicate images in the same image container!'
    
    logger.info("*********You have no duplicates in images for img*********")

#Checks to see if there are any invalid or missing tel: URI scheme for each contact card
def test_contact_cards_phone(driver):
    main_page = MainPage(driver)
    main_page.click_agree_cookie()
    contact_card_info = main_page.get_contact_cards_phone()

    if contact_card_info.startswith('Missing'): 
        logger.info(f"*********{contact_card_info}*********")
        assert False, 'Missing valid phone number tel: URI scheme in a contact card'
    elif contact_card_info.startswith('All'):
        logger.info("*********All contact cards have valid tel: URI scheme*********")
        assert True

#Checks to see if there are any invalid or missing mailto: URI scheme for each contact card
def test_contact_cards_email(driver):
    main_page = MainPage(driver)
    main_page.click_agree_cookie()
    contact_card_info = main_page.get_contact_cards_email()

    logger.info(f"{contact_card_info}")

    if contact_card_info.startswith('Missing'):
        logger.info(f"*********{contact_card_info}*********")
        assert False, 'Missing valid mailto: URI scheme in a contact card'
    elif contact_card_info.startswith('All'):
        logger.info("*********All contact cards have valid mailto: URI scheme*********")
        assert True

'''
Testing proper redirection of social media links
'''
def test_instagram_link(driver):
    main_page = MainPage(driver)
    expected_url = 'https://www.instagram.com/lighthouse_properties/'
    original_window = driver.current_window_handle #Returns a string of the current url, used for comparison
   
    
    main_page.click_agree_cookie()
    main_page.click_instagram()
    logger.info("*********Clicked Instagram link*********")
    
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )
    
    #window_handle = Returns a list of all currently open windows handles at the time it is called
    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    
    WebDriverWait(driver, 10).until(
        EC.url_to_be('https://www.instagram.com/lighthouse_properties/')
    )

    current_url = driver.current_url
    logger.info(f"*********Current url: {current_url}*********")
    
    if current_url == expected_url:
        logger.info("*********Redirected to Instagram page successfully*********")
        assert True
    else:
        logger.info("*********Redirection to Instagram page unsuccessful*********")
        assert False, 'Redirection to Instagram page unsuccessful'

def test_facebook_link(driver):
    main_page = MainPage(driver)
    expected_url = 'https://www.facebook.com/LighthousePropertiesVentspils'
    original_window = driver.current_window_handle #Returns a string of the current url, used for comparison
   
    
    main_page.click_agree_cookie()
    main_page.click_facebook()
    logger.info("*********Clicked Facebook link*********")
    
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )
    
    #window_handle = Returns a list of all currently open windows handles at the time it is called
    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    
    WebDriverWait(driver, 10).until(
        EC.url_to_be('https://www.facebook.com/LighthousePropertiesVentspils')
    )

    current_url = driver.current_url
    logger.info(f"*********Current url: {current_url}*********")
    
    if current_url == expected_url:
        logger.info("*********Redirected to Facebook page successfully*********")
        assert True
    else:
        logger.info("*********Redirection to Facebook page unsuccessful*********")
        assert False, 'Redirection to Facebook page unsuccessful'

'''
Tests to see if we have redirected to the appropriate office location on google maps
'''
#Tests to see if we successfully redirected to the Riga office location on google maps
def test_riga_office(driver):
    main_page = MainPage(driver)
    #Becuase google dynamically changes their links these two components in the url should remain the same. So we use these for comparison
    expected_url_part = 'https://www.google.com/maps'
    expected_url_place = 'Str%C4%93lnieku%20iela%205' 
    original_window = driver.current_window_handle #Returns a string of the current url, used for comparison
   

    main_page.click_agree_cookie()
    main_page.click_riga_office()
    logger.info("*********Clicked Riga Office link*********")
   
    
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )

    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    

    current_url = driver.current_url
    logger.info(f"*********Current url: {current_url}*********")
    
    if (expected_url_part in current_url) and (expected_url_place in current_url):
        logger.info("*********Redirected to google maps for Riga office location successfully*********")
        assert True
    else:
        logger.info("*********Redirection to google maps for Riga office location unsuccessful*********")
        assert False, 'Redirection to google maps for Riga office location unsuccessful'

#Tests to see if we successfully redirected to the Ventspils office location on google maps
def test_ventspils_office(driver):
    main_page = MainPage(driver)
    #Becuase google dynamically changes their links these two components in the url should remain the same. So we use these for comparison
    expected_url_part = 'https://www.google.com/maps'
    expected_url_place = 'Ventspils'
    original_window = driver.current_window_handle #Returns a string of the current url, used for comparison
   

    main_page.click_agree_cookie()
    main_page.click_ventspils_office()
    logger.info("*********Clicked Ventspils Office link*********")
   
    
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )

    logger.info(f"DELETE: Found two windows")

    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    
    logger.info("DELETE: We successfully switched window")

   

    logger.info("DELETE: The url is now set to be google maps")

    current_url = driver.current_url
    logger.info(f"*********Current url: {current_url}*********")
    
    if (expected_url_part in current_url) and (expected_url_place in current_url):
        logger.info("*********Redirected to google maps for Ventspils office location successfully*********")
        assert True
    else:
        logger.info("*********Redirection to google maps for Ventspils office location unsuccessful*********")
        assert False, 'Redirection to google maps for Ventspils office location unsuccessful'