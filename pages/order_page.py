from selenium.webdriver.common.by import By


class OrderPage:
    NAME = [By.XPATH, ".//input[@placeholder='* Имя']"]
    SURNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    PHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    DATE = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-placeholder"]
    RENTAL_OPTION = [By.XPATH, ".//div[text()='сутки']"]
    COLOR_BLACK = [By.ID, "black"]
    COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(text(),'Заказать')]"]
    CONFIRM_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    def __init__(self, driver):
        self.driver = driver

    def fill_first_page(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.SURNAME).send_keys(surname)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.METRO).send_keys(metro)
        self.driver.find_element(*self.METRO).click()
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_page(self, date, comment):
        self.driver.find_element(*self.DATE).send_keys(date)
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        self.driver.find_element(*self.RENTAL_OPTION).click()
        self.driver.find_element(*self.COLOR_BLACK).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BUTTON).click()
        self.driver.find_element(*self.CONFIRM_BUTTON).click()
