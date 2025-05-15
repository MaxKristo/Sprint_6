from selenium.webdriver.common.by import By

class MainPageLocators:    # класс содержит локаторы главной страницы

    question_locator = (By.XPATH, "//div[@id='accordion__heading-{}']")
    answer_locator = (By.XPATH, "//div[@id='accordion__panel-{}']")
    last_question_locator_to_scroll = (By.XPATH, "//div[@id='accordion__heading-7']")

    # Кнопка "Заказать" в теле страницы
    button_order_locator = By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    check_yandex_dzen = By.XPATH, './/*[@class="dzen-layout--navigation-tab__tabWrapper-3L"]'