from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.action_chains import ActionChains
from ui_tests.locators import general_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def is_visible(self, locator, timeout=10):
        with allure.step(f"Проверяется отображение элемента с локатором : {locator}"):
            try:
                element =  WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((locator.by, locator.value))
                )
                self.logger.debug(
                    f"{self.class_name}: Отображён элемент с локатором: {locator}"
                )
                return element
            except TimeoutException as e:
                self.logger.error(
                    f"{self.class_name}: Ошибка при нахождении элемента по локатору: {locator}"
                )
                raise e

    def input_value(self, locator, value, timeout=10):
        with allure.step(f"Вводится значение: {value}  в локатор {locator}"):
            try:
                find_field = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((locator.by, locator.value))
                )
                find_field.clear()
                find_field.click()
                find_field.send_keys(value)
                self.logger.debug(
                    f"{self.class_name}: Введён текст `{value}` в элемент с локатором: {locator}"
                )
            except Exception as e:
                self.logger.error(
                    f"{self.class_name}: Ошибка при вводе текста в элемент с локатором: {locator}"
                )
                raise e

    def click(self, button_text=None, locator=None, timeout=10, use_js=False):
        with allure.step(
                f"Нажимается {'элемент с локатором: ' + str(locator) if locator else 'кнопка с текстом: ' + str(button_text)}"
                ):
            try:
                if button_text:
                    locator = general_locators.BUTTON.format(value=button_text)

                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((locator.by, locator.value))
                )
                if use_js:
                    self.driver.execute_script("arguments[0].click();", element)
                    self.logger.debug(
                        f"{self.class_name}: JS-клик по элементу с локатором: {locator}"
                    )
                else:
                    element.click()
                    self.logger.debug(
                        f"{self.class_name}: Клик по элементу с локатором: {locator}"
                    )
            except Exception as e:
                self.logger.error(f"Ошибка при клике на элемент по локатору {locator}")
                raise e

    def get_elements(self, locator, timeout=10):
        with allure.step(f"Ожидание элементов по локатору: {locator}"):
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((locator.by, locator.value))
                )
            except Exception as e:
                self.logger.error(
                    f"{self.class_name}: Ошибка при нахождении элементов в HTML странице по локатору: {locator}"
                )
                raise e

    def scroll_to(self, button_text=None, locator=None, timeout=10, use_js=False):
        with allure.step(
                f"Скролл к {'элементу с локатором: ' + str(locator) if locator else 'кнопке с текстом: ' + str(button_text)}"
        ):
            try:
                if button_text:
                    locator = general_locators.BUTTON.format(value=button_text)

                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((locator.by, locator.value))
                )
                if use_js:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                               element)
                else:
                    ActionChains(self.driver).move_to_element(element).perform()
                    self.logger.debug(
                        f"{self.class_name}: Страница прокручена к элементу с локатором: {locator}"
                    )
            except Exception as e:
                self.logger.error(
                    f"{self.class_name}: Ошибка при скроле к элементу с локатором: {locator}"
                )
                raise e

    def pause(self, timeout):
        with allure.step(f"Пауза для загрузки страницы {timeout} сек."):
            try:
                ActionChains(self.driver).pause(timeout).perform()
                self.logger.debug(
                    f"{self.class_name}: Пауза для загрузки страницы {timeout} сек."
                )
            except Exception as e:
                self.logger.error(f"{self.class_name}: Ошибка при паузе в тесте.")
                raise e

    def click_collapse_menu(self):
        self.pause(1)
        self.click(locator=general_locators.COLLAPSE_MENU)
        self.pause(1)

