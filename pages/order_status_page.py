import allure
from pages.base_page import BasePage
from locators import *

class OrderStatusPage(BasePage):

    @allure.step('Ожидает появления окна успешного оформления заказа')        
    def wait_for_success_popup(self):
        return self.find_visible_element(OrderStatusPageLocators.SUCCESS_TITLE)

    @allure.step('Проверяем факт оформления заказа путем проверки отображения заголовка в окне успешного оформления заказа')
    def is_order_created(self):
        return self.wait_for_success_popup().is_displayed()
