import allure
from pages.base_page import BasePage
from locators import *

class MainPage(BasePage):
    # ---------- ВОПРОСЫ ---------
    @allure.step('Находим очередной вопрос на странице, прокручиваем до него и кликаем на вопросе')
    def click_question(self, index):
         self.scroll_and_click(MainPageLocators.QUESTION(index))

    @allure.step('Получаем текст очередного ответа')
    def get_answer_text(self, index):
        element = self.find_visible_element(MainPageLocators.ANSWER(index))
        return element.find_element(By.TAG_NAME, "p").text

    # ---------- ЗАКАЗ ----------
    @allure.step('Клик на кнопку заказа на главной странице')
    def click_order_bottom(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON_BOTTOM)