from selenium.webdriver.common.by import By

class MainPageLocators:
     # Логотипы
    SCOOTER_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]                             #Логотип "Самокат"
    YANDEX_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]                               #Логотип "Яндекс"  

    # Кнопки заказа
    ORDER_BUTTON_TOP = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]               #Кнопка "Заказать" в шапке
    ORDER_BUTTON_BOTTOM = [By.XPATH, ".//button[contains(@class,'Button_Middle')]"]         #Кнопка "Заказать" на странице

class OrderPageLocators:
    #Поля формы заказа первого шага
    NAME = [By.XPATH, ".//input[@placeholder='* Имя']"]                                     #Поле "Имя"
    SURNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"]                              #Поле "Фамилия"
    ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]           #Поле "Адрес заказа"    
    METRO = [By.XPATH, ".//input[contains(@placeholder, 'Станция метро')]"]                 #Поле "Станция метро"
    METRO_LIST_ITEM=[By.XPATH,".//input[contains(@placeholder, 'Станция метро')]/parent::div[@class='select-search__value']/following-sibling::div[@class='select-search__select']/ul/li[position()=1]/button"] #Поле "Пункт списка станций метро"
    PHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]       #Поле "Телефон"
    NEXT_BUTTON = [By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button"]             #Кнопка перехода на второй шаг

    #Поля формы заказа второго шага
    DATE = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]                  #Поле "Дата"
    DATEPICKER_SELECTED = [By.CLASS_NAME, "react-datepicker__day--selected"]                #Активный пункт календаря для снятия фокуса с модалки календаря
    RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-placeholder"]                                 #Поле "Период аренды"
    RENTAL_OPTION = [By.XPATH, ".//div[text()='сутки']"]                                    #Пункт списка поля "Период аренды"

    COLOR_BLACK = [By.ID, "black"]                                                          #Флажок выбора цвета самоката
    COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]                #Поле "Комментарий"
    ORDER_BUTTON = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Заказать')]"] #Кнопка "Заказать" на форме заказа
    CONFIRM_BUTTON = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']//button[text()='Да']"]                #Кнопка подтверждения заказа

class OrderStatusPageLocators:
    SUCCESS_TITLE = [By.XPATH, ".//div[contains(text(),'Заказ оформлен')]"]                 #Заголовок модального окна успешного заказа
    VIEW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]                #Кнопка просмотра статуса заказа