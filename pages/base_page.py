import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

# поиск элемента
    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 8).until(expected_conditions.presence_of_element_located(locator))

# клик по элементу
    @allure.step('Кликнуть элемент')
    def click_to_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

# скроллинг до элемента и ожидание его кликабельности
    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        return element

# получение текста из элемента
    @allure.step('Получаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

# метод передаёт тест элементу
    @allure.step('Изменить текст')
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def format_locator(self, locator, text):
        by, locator_str = locator
        locator_str = locator_str.format(text)
        return by, locator_str

    @allure.step("Дождаться открытия новой вкладки и перейти на нее")
    def switch_and_get_url(self):
        self.wait.until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Проверяем кликабельность кнопки в окне с куками')
    def windows_cookies(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

# метод открывает переданную страницу
    @allure.step('Открываем переданную страницу')
    def go_to_url(self, url):
        self.driver.get(url)