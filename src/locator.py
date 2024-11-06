from selenium.webdriver.common.by import By

class MainPageLocators(object):
    #Inital Prompt
    AGREE_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Piekrītu']]")
    REJECT_COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'cookie-consent-button') and span[text()='Noraidīt']]")
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(text(), 'privātuma politiku')]")
    PRIVACY_POLICY_LINK_SECOND = (By.XPATH, "//a[contains(text(), 'Lasīt privātuma politiku')]")
   
    #Navigation bar
    HOME_PAGE_BUTTON = (By.XPATH, "//img[contains(@class,'logo-img')]")
    TO_THE_SELLER_LINK = (By.XPATH, "//a[contains(text(), 'Pārdevējam')]")
    TO_THE_BUYER_LINK = (By.XPATH, "//a[contains(text(), 'Pircējam')]")
    ABOUT_US_LINK = (By.XPATH, "//a[contains(text(), 'Par mums')]")
    
    #Property section on page
    PROPERTY_CARD_GRID_CONTAINER = (By.CLASS_NAME, 'property-card-grid-container')
    PROPERTY_CARDS = (By.XPATH,"//div[contains(@class, 'property-card-container') and contains(@class, 'show')]")
    NEXT_PROPERTY_PAGE_BUTTON = (By.XPATH, "(//button[contains(@class, 'switch-page-button')])[2]") #selects 2 button since no distinction between two buttons
    PREVIOUS_PROPERTY_PAGE_BUTTON = (By.XPATH, "(//button[contains(@class, 'switch-page-button')])[1]") 
    PROPERTY_PAGE_COUNT_TEXT = (By.XPATH, "//span[@class = 'page-buttons-text']")
    
    #Property type buttons
    PRIVATMAJAS_BUTTON = (By.XPATH, "//button[contains(text(), 'Privātmājas')]")
    DZIVOKLI_BUTTON = (By.XPATH, "//button[contains(text(), 'Dzīvokļi')]")
    KOMERCIPASUMI_BUTTON = (By.XPATH, "//button[contains(text(), 'Komercīpašumi')]")
    ZEMES_BUTTON = (By.XPATH, "//button[contains(text(), 'Zemes')]")

    #Contact card information
    CONTACT_CARD = (By.XPATH,"//div[@class= 'contact-card']")

    #Social media links
    INSTAGRAM_LINK = (By.XPATH,"//a[contains(@href, 'https://www.instagram.com/lighthouse_properties')]")
    FACEBOOK_LINK = (By.XPATH,"//a[contains(@href, 'https://www.facebook.com/LighthousePropertiesVentspils')]")

    #Office location links
    RIGA_OFFICE = (By.XPATH,"//a[contains(@href, 'https://www.google.com/maps/search/?api=1&query=Strēlnieku iela 5, Centra rajons, Rīga, LV-1010, Latvia')]")
    VENTSPILS_OFFICE = (By.XPATH, "//a[contains(@href, 'https://www.google.com/maps/search/?api=1&query=Kuldīgas iela 17, Ventspils, Latvia')]")

class PropertyPageLocators(object):
    #Viewing property
    LEFT_IMAGE_ARROW = (By.XPATH,"//div[contains(@class, 'scroll-button-left-container')]")
    RIGHT_IMAGE_ARROW = (By.XPATH,"//div[contains(@class, 'scroll-button-right-container')]")
    PROPERTY_CARDS = (By.XPATH,"//div[contains(@class, 'property-card-container') and contains(@class, 'show')]")
    PROPERTY_IMAGES = (By.XPATH,"//div[contains(@class, 'small-image-wrap')]")
    SELECTED_PROPERTY_IMAGE = (By.XPATH,"//div[contains(@class, 'small-image-wrap') and contains(@class, 'selected-image')]")
    
#Each class represents a new pages locators. If you want to test a specific page add new locators here