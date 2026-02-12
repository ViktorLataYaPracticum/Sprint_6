import allure
from pages.base_page import BasePage
from locators import *

class OrderPage(BasePage):

    @allure.step('Заполняем поля первого шага формы заказа. Клик на кнопке "Далее"')
    def fill_first_page(self, name, surname, address, metro, phone):
        self.fill_input(OrderPageLocators.NAME,name)
        self.fill_input(OrderPageLocators.SURNAME,surname)
        self.fill_input(OrderPageLocators.ADDRESS,address)
        self.click_element(OrderPageLocators.METRO)
        self.fill_input(OrderPageLocators.METRO,metro)
        self.click_element(OrderPageLocators.METRO_LIST_ITEM)
        self.find_element(OrderPageLocators.PHONE).clear()
        self.fill_input(OrderPageLocators.PHONE,phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем поля второго шага формы заказа. Клик на кнопке "Заказать"')
    def fill_second_page(self, date, comment):
        self.fill_input(OrderPageLocators.DATE,date)
        self.click_element(OrderPageLocators.DATEPICKER_SELECTED)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
        self.click_element(OrderPageLocators.COLOR_BLACK)
        self.fill_input(OrderPageLocators.COMMENT,comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)