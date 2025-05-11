import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


# класс содержит методы страницы заказа и наследует базовые методы
class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# клик по полю и ввод в него значения
    @allure.title('Клик по полю и его заполнение')
    def fill_text_field(self, locator, text):
        self.click_to_element(locator)
        self.set_text(locator, text)

# заполнение формы "Для кого самокат"
    @allure.title('Заполнение формы "Для кого самокат"')
    @allure.description('Заполнение полей - "Имя", "Фамилия", "Адрес", "Телефон" и выбор из выпадающего списка станции метро "Пушкинская"')
    def fill_form_who_is_the_scooter_for(self, user):
        self.fill_text_field(OrderPageLocators.fields_name_locator, user["name"])
        self.fill_text_field(OrderPageLocators.fields_last_name_locator, user["surname"])
        self.fill_text_field(OrderPageLocators.fields_address_locator, user["address"])
        self.click_to_element(OrderPageLocators.fields_metro_station_locator)
        self.click_to_element(OrderPageLocators.fields_metro_station_1_locator)
        self.fill_text_field(OrderPageLocators.fields_telephone_locator, user["phone"])
        self.click_to_element(OrderPageLocators.button_next_locator)

# заполнение формы "Про аренду"
    @allure.title('Заполнение формы "Про аренду"')
    @allure.description('Заполнение поля - "Комментарий" и выбор "Даты начала аренды" из календаря, "Срока аренды" из выпадающего списка и выбор цвета самоката в чек боксе')
    def fill_form_about_rent(self, user):
        self.click_to_element(OrderPageLocators.field_date_locator)
        self.click_to_element(OrderPageLocators.choose_rent_day_locator)
        self.click_to_element(OrderPageLocators.field_rental_period_locator)
        self.click_to_element(OrderPageLocators.choose_rent_period_locator)
        self.click_to_element(OrderPageLocators.choose_black_color_locator)
        self.fill_text_field(OrderPageLocators.field_comment_locator, user["comment"])
        self.click_to_element(OrderPageLocators.button_place_order_locator)


