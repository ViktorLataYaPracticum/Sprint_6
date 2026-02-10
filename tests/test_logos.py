import allure
import time
from pages.main_page import MainPage
from constants import Constants

class TestLogos:

    @allure.step('Тест перехода на главную страницу сервиса при нажатии на логотип "Самокат" в шапке страницы сервиса ')
    def test_scooter_logo_redirects_to_main_page(self,driver):
        page = MainPage(driver)
        page.click_scooter_logo()
        assert driver.current_url == Constants.SERVICE_URL

    @allure.step('Тест перехода на целевую страницу при нажатии на логотип "Яндекс" в шапке страницы сервиса ')
    def test_yandex_logo_opens_dzen(self,driver):
        page = MainPage(driver)
        page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)
        assert Constants.DZEN_URL in driver.current_url
