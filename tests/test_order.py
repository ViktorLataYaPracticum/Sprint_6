import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.order_status_page import OrderStatusPage
from test_data import OrderFormData

class TestOrderScooter:

    @allure.title('Тест оформления заказа при нажатии на кнопку заказа в шапке страницы сервиса')
    @pytest.mark.parametrize("user_data", OrderFormData.VALID_DATA)
    def test_order_scooter_click_button_in_header(self,driver, user_data):
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        status_page = OrderStatusPage(driver)
        base_page.click_order_top()
        order_page.fill_first_page(*user_data[:5])
        order_page.fill_second_page(user_data[5], user_data[6])
        assert status_page.is_order_created()

    @allure.title('Тест оформления заказа при нажатии на кнопку заказа на главной странице сервиса')
    @pytest.mark.parametrize("user_data", OrderFormData.VALID_DATA)
    def test_order_scooter_click_button_on_page(self,driver, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_bottom()
        status_page = OrderStatusPage(driver)
        order_page.fill_first_page(*user_data[:5])
        order_page.fill_second_page(user_data[5], user_data[6])
        assert status_page.is_order_created()    
