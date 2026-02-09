from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import *

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ---------- ВОПРОСЫ ----------
    def click_question(self, index):
        question = self.wait.until(
        EC.presence_of_element_located((By.XPATH,f".//div[@class='accordion']/div[position()={(index+1)} and @class='accordion__item']/div"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.wait.until(EC.element_to_be_clickable(question)).click()

    def get_answer_text(self, index):
        item=self.wait.until(
            EC.visibility_of_element_located((By.ID, f"accordion__panel-{index}"))
        )
        item=self.driver.find_element(By.ID, f"accordion__panel-{index}")    
        return item.find_element(By.TAG_NAME, "p").text

    # ---------- ЗАКАЗ ----------
    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_TOP)).click()

    def click_order_bottom(self):
        button=self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", button) 
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)).click()

    # ---------- ЛОГОТИПЫ ----------
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)).click()
