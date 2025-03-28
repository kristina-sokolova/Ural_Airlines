import random

from ui_tests.pages.base_page import BasePage
import allure

from ui_tests.tests.test_data import PikInFilter
from ui_tests.locators import service_requests_locators


class ServiceRequests(BasePage):

    def click_random_queue(self, value=None):
        filtered_queues = [queue for queue in PikInFilter.list_of_queue if
                           queue != "Претензии" and queue != "Все претензии" and queue != "Прослушка звонка (В работе)"]
        value = random.choice(filtered_queues)
        self.scroll_to(value, use_js=True)
        self.click(value)
        self.pause(2)

    def click_on_button_in_zo_screen(self, button):
        with allure.step(f"Нажимается кнопка {button} на экране Запросы на обслуживание"):
            self.pause(2)
            self.click(locator=service_requests_locators.BUTTON_IN_ZO.format(value=button), use_js=True)

    def click_with_pause(self, value):
        self.pause(1)
        self.click(value)
        self.pause(1)

    def get_type_elements_in_filter(self):
        with allure.step(
                "Получение элементов из выпадающего списка"
        ):
            elements = self.get_elements(service_requests_locators.TYPE_ELEMENTS_IN_FILTER)
            titles = [i.text for i in elements]
            return titles

    def click_random_queue_with_plus_icon(self, value=None):
        filtered_queues = [queue for queue in PikInFilter.list_of_queue if
                           queue != "Прослушка звонка (В работе)" and queue != "Мои запросы" and queue != "Все претензии" and queue != "Очередь кассиров"]
        value = random.choice(filtered_queues)
        self.scroll_to(value, use_js=True)
        self.click(value)
        self.pause(2)


    def click_random_queue_for_pick_list_in_zo_card(self, value=None):
        filtered_queues = [queue for queue in PikInFilter.list_of_queue if
                           queue != "Прослушка звонка (В работе)" and queue != "Мои запросы" and queue != "Все претензии" and queue != "Очередь кассиров" and queue != "Претензии" and queue != "Все запросы"]
        value = random.choice(filtered_queues)
        self.scroll_to(value, use_js=True)
        self.click(value)
        self.pause(2)

    def click_on_field_in_modal_window_add_new_service_request(self, field):
        with allure.step(f"Нажимается поле {field} в модальном окне на добавление нового запроса на обслуживание"):
            self.pause(2)
            self.click(locator=service_requests_locators.REQUIRED_FIELD_CREATE_SERVICE_REQUEST.format(value=field),
                       use_js=True)
