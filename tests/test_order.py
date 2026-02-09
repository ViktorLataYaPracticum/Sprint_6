from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_status_page import OrderStatusPage
import pytest
from selenium import webdriver
from constants import Constants

class TestOrderScooter:
    #Для теста формы заказа скутера для каждого набора данных создаем новый элемент драйвера браузера
    
    @pytest.mark.parametrize("button", ["top",
                                        "bottom"
                                        ]
                                        )
    @pytest.mark.parametrize("user_data", [
        ("Иван", "Иванов", "Москва", "Сокольники", "89991112233", "10.02.2026", "Без звонка"),
        ("Петр", "Петров", "Питер", "Парк Победы", "89990001122", "15.02.2026", "Позвонить заранее")
    ])
    def test_order_scooter(self,driver, button, user_data):
        main_page = MainPage(driver)
        
        if button == "top":
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

        order_page = OrderPage(driver)
        order_page.fill_first_page(*user_data[:5])
        order_page.fill_second_page(user_data[5], user_data[6])

        status_page = OrderStatusPage(driver)
        assert status_page.is_order_created()
