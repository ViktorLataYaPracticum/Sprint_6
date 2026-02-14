import allure
from pages.main_page import MainPage

class TestLogos:

    @allure.title('Тест перехода на главную страницу сервиса при нажатии на логотип "Самокат" в шапке страницы сервиса ')
    def test_scooter_logo_redirects_to_main_page(self,driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page_via_logo()
        assert main_page.is_main_page_opened()

    @allure.title('Тест перехода на целевую страницу при нажатии на логотип "Яндекс" в шапке страницы сервиса ')
    def test_yandex_logo_opens_dzen(self,driver):
        main_page = MainPage(driver)
        main_page.go_to_dzen_via_yandex_logo()
        assert main_page.is_dzen_opened()   