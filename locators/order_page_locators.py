from selenium.webdriver.common.by import By
from data import day_str


class OrderPageLocators:   # класс содержит локаторы страницы "Заказать"
    # кнопка "Далее"
    button_next_locator = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Далее")]'
    # кнопка "Заказать"_(в блоке заказа)
    button_place_order_locator = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Заказать")]'
    # поле "Имя"
    fields_name_locator = By.XPATH, "//input[@placeholder='* Имя']"
    # поле "Фамилия"
    fields_last_name_locator = By.XPATH, "//input[@placeholder='* Фамилия']"
    # поле "Адрес"
    fields_address_locator = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # поле "Станция метро"
    fields_metro_station_locator = By.XPATH, "//input[@placeholder='* Станция метро']"
    # Поле "Станция метро" - станция Пушкинская
    fields_metro_station_1_locator = By.XPATH, "//div[@class='Order_Text__2broi' and text()='Пушкинская']"
    # Поле "Станция метро" - станция Спортивная
    fields_metro_station_2_locator = By.XPATH, "//div[@class='Order_Text__2broi' and text()='Спортиная']"
    # поле "Телефон"
    fields_telephone_locator = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # поле "Когда привезти самокат"
    field_date_locator = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # выбор даты когда привезти самокат из выпадающего календаря
    choose_rent_day_locator = By.XPATH, f"//div[contains(@aria-label, '{day_str}-е мая 2025')]"
    # поле "Срок аренды"
    field_rental_period_locator = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    # выбор срока аренды из выпадающего списка
    choose_rent_period_locator = By.XPATH, ".//div[text()='трое суток']"
    # выбор цвета самоката "чёрный жемчуг"
    choose_black_color_locator = (By.ID, "black")
    # поле "Комментарий"
    field_comment_locator = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # кнопка "Да" в окне "Хотите оформить заказ"
    button_yes_locator = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Да")]'
    # окно "Заказ оформлен"
    window_confirmation_order_locator = By.XPATH, ".//div[text()='Заказ оформлен']"
    # кнопка "Посмотреть статус" в окне "Заказ оформлен"
    button_view_status_locator = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Посмотреть статус")]'



