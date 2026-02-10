import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поля первого шага формы заказа. Клик на кнопке "Далее"')
    def fill_first_page(self, name, surname, address, metro, phone):
        self.driver.find_element(*OrderPageLocators.NAME).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS).send_keys(address)
        self.driver.find_element(*OrderPageLocators.METRO).click()
        self.driver.find_element(*OrderPageLocators.METRO).send_keys(metro)
        self.driver.find_element(*OrderPageLocators.METRO_LIST_ITEM).click()
        self.driver.find_element(*OrderPageLocators.PHONE).clear()
        self.driver.find_element(*OrderPageLocators.PHONE).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполняем поля второго шага формы заказа. Клик на кнопке "Заказать"')
    def fill_second_page(self, date, comment):
        self.driver.find_element(*OrderPageLocators.DATE).send_keys(date)
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATEPICKER_SELECTED)).click() 
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_OPTION).click()
        self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(comment)
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)).click()
