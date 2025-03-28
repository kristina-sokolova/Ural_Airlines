from ui_tests.pages.base_page import BasePage
from ui_tests.locators import general_locators
from dotenv import load_dotenv
import os

load_dotenv()


class LoginPage(BasePage):

    def login(self):
        self.input_value(general_locators.FIELD.format(value="Логин"), os.getenv("LOGIN_PETROV"))
        self.input_value(general_locators.FIELD.format(value="Пароль"), os.getenv("PASS_PETROV"))
        self.click("Войти")
        self.pause(25)


