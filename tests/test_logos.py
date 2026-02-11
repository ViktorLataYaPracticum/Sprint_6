import allure
import time
from pages.base_page import BasePage
from pages.main_page import MainPage
from constants import Constants

class TestLogos:

    @allure.step('Тест перехода на главную страницу сервиса при нажатии на логотип "Самокат" в шапке страницы сервиса ')
    def test_scooter_logo_redirects_to_main_page(self,driver):
        page = MainPage(driver)
        base_page = BasePage(driver)
        page.click_scooter_logo()
        assert base_page.get_current_url() == Constants.SERVICE_URL

    @allure.step('Тест перехода на целевую страницу при нажатии на логотип "Яндекс" в шапке страницы сервиса ')
    def test_yandex_logo_opens_dzen(self,driver):
        page = MainPage(driver)
        base_page = BasePage(driver)
        page.click_yandex_logo()
        base_page.switch_to_window()
        time.sleep(10)
        assert Constants.DZEN_URL in base_page.get_current_url()
