import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    @allure.step('Поиск элемента по locator с ожиданием появления элемента на странице')
    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    @allure.step('Заполнение элемента locator текстом text с ожиданием появления элемента на странице')
    def fill_input(self, locator,text):
        self.find_element(locator).send_keys(text)
            
    @allure.step('Поиск элемента по locator с ожиданием отображения элемента на странице')
    def find_visible_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    @allure.step("Клик по элементу только при его наличии на странице")  
    def click_presents_element(self,locator):
        try:
            self.wait.until(
                EC.presence_of_element_located(locator)
            ).click()
        except TimeoutException:
            pass  # элемента нет — ничего не делаем
  
    @allure.step('Клик по элементу locator с ожиданием его clickable')
    def click_element(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
        
    @allure.step('Скролл до элемента element')
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        
    @allure.step('Скролл до элемента locator с последующим кликом по нему')    
    def scroll_and_click(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.click_element(locator)
        
    @allure.step('Получаем текущий url')    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключаемся по вкладкам браузера, по умолчанию на первую')    
    def switch_to_window(self, index=1):
        self.driver.switch_to.window(self.driver.window_handles[index])
        
    @allure.step('Ожидаем появления второй вкладки и переходим на вкладку 1')        
    def wait_for_new_window_and_switch(self, timeout=10):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.switch_to_window(1)
    
    @allure.step('Ожидаем появления искомого текста в url')
    def wait_for_url_contains(self, text):
        self.wait.until(
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
        
    @allure.step('Клик по кнопке согласия с куками, на маленьком экране панель с куками перекрывает кнопку перехода на второй этап оформления')
    def click_coockie_button(self):
        self.click_presents_element(BasePageLocators.COOCKIE_BUTTON)      