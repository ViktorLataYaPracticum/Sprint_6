import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import *

class OrderStatusPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидает появления окна успешного оформления заказа')        
    def wait_for_success_popup(self):
        self.wait.until(EC.visibility_of_element_located(OrderStatusPageLocators.SUCCESS_TITLE))

    @allure.step('Проверяем факт оформления заказа путем проверки отображения заголовка окна успешного оформления заказа')
    def is_order_created(self):
        self.wait_for_success_popup()
        return self.driver.find_element(*OrderStatusPageLocators.SUCCESS_TITLE).is_displayed()
