from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderStatusPage:
    SUCCESS_TITLE = [By.XPATH, ".//div[contains(text(),'Заказ оформлен')]"]
    VIEW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_success_popup(self):
        """
        Ожидает появления окна успешного оформления заказа
        """
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TITLE))

    def is_order_created(self):
        self.wait_for_success_popup()
        return self.driver.find_element(*self.SUCCESS_TITLE).is_displayed()
