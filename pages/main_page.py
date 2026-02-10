import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import *

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    # ---------- ВОПРОСЫ ---------
    @allure.step('Находим очередной вопрос на странице, прокручиваем до него и кликаем на вопросе')
    def click_question(self, index):
        question = self.wait.until(
        EC.presence_of_element_located((By.XPATH,f".//div[@class='accordion']/div[position()={(index+1)} and @class='accordion__item']/div"))
        )
        self.scrollToElement(question)
        self.wait.until(EC.element_to_be_clickable(question)).click()

    @allure.step('Получаем текст очередного ответа')
    def get_answer_text(self, index):
        item=self.wait.until(
            EC.visibility_of_element_located((By.ID, f"accordion__panel-{index}"))
        )
        return item.find_element(By.TAG_NAME, "p").text

    # ---------- ЗАКАЗ ----------
    
    @allure.step('Клик на кнопку заказа на главной странице')
    def click_order_bottom(self):
        button=self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.scrollToElement(button)
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)).click()