from selenium.webdriver.common.by import By

class BasePageLocators:

    button_order_header_locator = By.CLASS_NAME, "Button_Button__ra12g"                    # Кнопка "Заказать" в заголовке страницы
    button_status_order_locator = By.CLASS_NAME, "Header_Link__1TAG7"                      # Кнопка "Статус заказа" в заголовке страницы
    button_scooter_locator = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]'           # логотип "Самокат" в заголовке страницы
    button_yandex_locator = By.XPATH, '//a[@class ="Header_LogoYandex__3TSOI"]'            # логотип "Яндекс" в заголовке страницы
    button_accept_cookie_locator = By.ID, "rcc-confirm-button"                             # кнопка принятия куки - "да все привыкли"
