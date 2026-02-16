import allure
from pages.base_page import BasePage
from locators import MainPageLocators,BasePageLocators
from urls import Urls

class MainPage(BasePage):
    # ---------- ВОПРОСЫ ---------
    @allure.step('Находим очередной вопрос на странице, прокручиваем до него и кликаем на вопросе')
    def click_question(self, index):
         self.scroll_and_click(MainPageLocators.QUESTION(index))

    @allure.step('Получаем текст очередного ответа')
    def get_answer_text(self, index):
        return self.find_visible_element(MainPageLocators.ANSWER(index)).text

    # ---------- ЗАКАЗ ----------
    @allure.step('Клик на кнопку заказа на главной странице')
    def click_order_bottom(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step('Переход на страницу Dzen по клику на логотип "Яндекс" в шапке страницы сервиса')
    def go_to_dzen_via_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)
        self.wait_for_new_window_and_switch()
        self.wait_for_url_contains(Urls.DZEN_URL) 
           
    @allure.step('Переход на главную страницу через логотип Самокат')
    def go_to_main_page_via_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Проверяем, что открыта главная страница сервиса')
    def is_main_page_opened(self):
        return self.get_current_url() == Urls.SERVICE_URL    
    
    @allure.step('Проверяем, что открыт Дзен')
    def is_dzen_opened(self):
        return Urls.DZEN_URL in self.get_current_url()
        
    @allure.step('Клик на кнопку "Заказать" в шапке страницы сервиса')
    def click_order_top(self):
        self.click_element(BasePageLocators.ORDER_BUTTON_TOP)
        
    @allure.step('Клик по кнопке согласия с куками, на маленьком экране панель с куками перекрывает кнопку перехода на второй этап оформления')
    def click_coockie_button(self):
        self.click_presents_element(BasePageLocators.COOCKIE_BUTTON)