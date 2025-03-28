import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService

import allure
from ui_tests.pages.base_page import BasePage
import requests
from requests.auth import HTTPBasicAuth

from ui_tests.pages.login_page import LoginPage
import logging
import datetime


@pytest.fixture()
def browser(request):
    local = request.config.getoption("--local")
    version = request.config.getoption("--bv")
    executor = request.config.getoption("--executor")

    if not local:

        executor_url = f"http://{executor}:4444/wd/hub"

        options = webdriver.ChromeOptions()

        logger = logging.getLogger(request.node.name)
        file_handler = logging.FileHandler("../../execution.log", encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
        logger.addHandler(file_handler)
        logger.setLevel(level=logging.DEBUG)
        logger.info("===> Тест %s начался в %s" % (request.node.name, datetime.datetime.now()))

        caps = {
            "browserVersion": version,
            "selenoid:options": {"enableVNC": True},
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        with allure.step(
                f"Подключение к удаленному веб-драйверу по адресу {executor_url}"
        ):
            driver = webdriver.Remote(
                command_executor=executor_url,
                options=options,
            )

        with allure.step("Максимизация окна браузера"):
            driver.maximize_window()

        driver.test_name = request.node.name
        driver.logger = logger

        with allure.step("Открывается страница Siebel CRM"):
            driver.get(os.getenv("BASE_URL"))

        yield driver

        with allure.step("Открытие DevTools и выполнение команды LogOff"):
            try:
                driver.execute_script("SiebelApp.S_App.LogOff();")
                logger.info("Команда SiebelApp.S_App.LogOff() успешно выполнена.")
            except Exception as e:
                logger.error(f"Ошибка при выполнении команды LogOff: {e}")

        with allure.step("Закрытие браузера и завершение сессии драйвера"):
            driver.quit()
        logger.info("===> Тест %s закончился в %s" % (request.node.name, datetime.datetime.now()))

    else:

        with allure.step("Открывается браузер Chrome"):
            driver = webdriver.Chrome(service=ChromiumService())

        logger = logging.getLogger(request.node.name)
        file_handler = logging.FileHandler("../../execution.log", encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
        logger.addHandler(file_handler)
        logger.setLevel(level=logging.DEBUG)
        logger.info("===> Тест %s начался в %s" % (request.node.name, datetime.datetime.now()))

        with allure.step("Максимизация окна браузера"):
            driver.maximize_window()

        driver.test_name = request.node.name
        driver.logger = logger

        with allure.step("Открывается страница Siebel CRM"):
            driver.get(os.getenv("BASE_URL"))

        yield driver

        with allure.step("Открытие DevTools, выполнение команды LogOff и нажатие Enter"):
            try:
                driver.execute_cdp_cmd("Runtime.evaluate", {
                    "expression": "SiebelApp.S_App.LogOff()"
                })
                logger.info("Команда SiebelApp.S_App.LogOff() успешно выполнена.")

                driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                    "type": "keyDown",
                    "key": "Enter",
                    "code": "Enter",
                    "text": "\r",
                    "unmodifiedText": "\r"
                })
                driver.execute_cdp_cmd("Input.dispatchKeyEvent", {
                    "type": "keyUp",
                    "key": "Enter",
                    "code": "Enter",
                    "text": "\r",
                    "unmodifiedText": "\r"
                })
                logger.info("Клавиша Enter успешно нажата.")
            except Exception as e:
                logger.error(f"Ошибка при выполнении команды LogOff или нажатии Enter: {e}")

        with allure.step("Закрытие браузера и завершение сессии драйвера"):
            driver.quit()
        logger.info("===> Тест %s закончился в %s" % (request.node.name, datetime.datetime.now()))


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs["browser"]
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture()
def login(browser):
    with allure.step("Заполняются поля логин и пароль"):
        LoginPage(browser).login()


@pytest.fixture()
def collapse_menu(browser):
    with allure.step("Нажимается кнопка для разворачивания/сворачивания меню"):
        BasePage(browser).click_collapse_menu()


@pytest.fixture()
def base_url_siebel():
    return os.getenv("SOAP_URL")


@pytest.fixture()
def get_authorization():
    username = os.getenv("LOGIN_PETROV")
    password = os.getenv("PASS_PETROV")

    res = requests.post(os.getenv("SOAP_URL"), auth=HTTPBasicAuth(username, password))

    if res.status_code == 200:
        print("Запрос выполнен успешно!")
        return res.json()
    else:
        print(f"Ошибка: {res.status_code} - {res.text}")

