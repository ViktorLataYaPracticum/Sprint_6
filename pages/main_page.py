from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    # Логотипы
    SCOOTER_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    YANDEX_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    # Кнопки заказа
    ORDER_BUTTON_TOP = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    ORDER_BUTTON_BOTTOM = [By.XPATH, ".//button[contains(@class,'Button_Middle')]"]

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
        return item.find_element(By.TAG_NAME, "p").text

    # ---------- ЗАКАЗ ----------
    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP)).click()

    def click_order_bottom(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM)).click()

    # ---------- ЛОГОТИПЫ ----------
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()
