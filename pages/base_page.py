import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_visible_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
    def scroll_and_click(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.click_element(locator)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self, index=1):
        self.driver.switch_to.window(self.driver.window_handles[index])
        
    def wait_for_new_window_and_switch(self, timeout=10):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step('Клик на кнопку "Заказать" в шапке страницы сервиса')
    def click_order_top(self):
        self.click_element(BasePageLocators.ORDER_BUTTON_TOP)

    @allure.step('Клик на логотип "Самокат" в шапке страницы сервиса')
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)
        
    @allure.step('Клик на логотип "Яндекс" в шапке страницы сервиса')
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)  