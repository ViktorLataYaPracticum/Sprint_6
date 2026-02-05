from selenium import webdriver
from pages.main_page import MainPage
from constants import Constants

class TestLogos:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(Constants.SERVICE_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_scooter_logo_redirects_to_main_page(self):
        page = MainPage(self.driver)
        page.click_scooter_logo()
        assert self.driver.current_url == Constants.SERVICE_URL

    def test_yandex_logo_opens_dzen(self):
        page = MainPage(self.driver)
        page.click_yandex_logo()

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "dzen.ru" in self.driver.current_url
