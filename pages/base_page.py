import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step('Прокрутка страницы до целевого элемента')
    def scrollToElement(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Клик на кнопку "Заказать" в шапке страницы сервиса')
    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(BasePageLocators.ORDER_BUTTON_TOP)).click()    

    # ---------- ЛОГОТИПЫ ----------
    @allure.step('Клик на лого "Самокат" в шапке страницы сервиса')
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(BasePageLocators.SCOOTER_LOGO)).click()

    @allure.step('Клик на лого "Яндекс" в шапке страницы сервиса')
    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(BasePageLocators.YANDEX_LOGO)).click()    
    
    def get_current_url(self):
        return self.driver.current_url
    
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])   
    