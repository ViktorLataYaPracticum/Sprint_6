from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class OrderStatusPage:
   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_success_popup(self):
        """
        Ожидает появления окна успешного оформления заказа
        """
        self.wait.until(EC.visibility_of_element_located(OrderStatusPageLocators.SUCCESS_TITLE))

    def is_order_created(self):
        self.wait_for_success_popup()
        return self.driver.find_element(*OrderStatusPageLocators.SUCCESS_TITLE).is_displayed()
