from selenium.webdriver.common.by import By

class MainPageLocators(object):
    AGREE_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Piekrītu']]")
    REJECT_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Noraidīt']]")
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(text(), 'privātuma politiku')]")
    PRIVACY_POLICY_LINK_SECOND = (By.XPATH, "//a[contains(text(), 'Lasīt privātuma politiku')]")

    TO_THE_SELLER_LINK = (By.XPATH, "//a[contains(text(), 'Pārdevējam')]")
    TO_THE_BUYER_LINK = (By.XPATH, "//a[contains(text(), 'Pircējam')]")
    ABOUT_US_LINK = (By.XPATH, "//a[contains(text(), 'Par mums')]")

    PROPERTY_CARD_GRID_CONTAINER = (By.CLASS_NAME, 'property-card-grid-container')
    PROPERTY_CARDS = (By.XPATH, "//div[contains(@class, 'property-card-container') and contains(@class, 'show')]")
    NEXT_PROPERTY_PAGE_BUTTON = (By.XPATH, "(//button[contains(@class, 'switch-page-button')])[2]") #selects 2 button since no distinction between two buttons
    PREVIOUS_PROPERTY_PAGE_BUTTON = (By.XPATH, "(//button[contains(@class, 'switch-page-button')])[1]") 
    PROPERTY_PAGE_COUNT_TEXT = (By.XPATH, "//span[@class = 'page-buttons-text']")
 
#Each class represents a new pages locators. If you want to test a specific page add new locators here