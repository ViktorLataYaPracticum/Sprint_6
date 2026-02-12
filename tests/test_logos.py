import allure
from pages.base_page import BasePage
from urls import Urls

class TestLogos:

    @allure.title('Тест перехода на главную страницу сервиса при нажатии на логотип "Самокат" в шапке страницы сервиса ')
    def test_scooter_logo_redirects_to_main_page(self,driver):
        base_page = BasePage(driver)
        base_page.click_scooter_logo()
        assert base_page.get_current_url() == Urls.SERVICE_URL

    @allure.title('Тест перехода на целевую страницу при нажатии на логотип "Яндекс" в шапке страницы сервиса ')
    def test_yandex_logo_opens_dzen(self,driver):
        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        base_page.wait_for_new_window_and_switch()
        base_page.wait_for_url_contains(Urls.DZEN_URL)
        assert Urls.DZEN_URL in base_page.get_current_url()
