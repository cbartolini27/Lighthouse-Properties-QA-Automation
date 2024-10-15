from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#Setting or Getting value of element - descripter class
class BasePageElement(object):
    def __init__(self,by,locator):
        self.by = by 
        self.locator = locator
    
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(self.by, self.locator)
        )
        driver.find_element(self.by, self.locator).clear()
        driver.find_element(self.by, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(self.by, self.locator)
        )
        element = driver.find_element(self.by, self.locator)
        return element.get_attribute("value")
        