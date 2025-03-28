from ui_tests.pages.base_page import BasePage
from ui_tests.pages.service_requests import ServiceRequests
import allure
from ui_tests.tests.test_data import PikInFilter
import pytest


@allure.epic("Тесты UI")
@allure.feature("Пик-листы")
@allure.title("Проверить пик-лист в рандомной очереди в фильтрации - Тип")
@pytest.mark.smoke
def test_check_types_in_filter(browser, login, collapse_menu):
    """Проверяем пик-лист в Запросах на обслуживание - Фильтр - Тип """
    page = ServiceRequests(browser)
    page.click("Запросы на обслуживание")
    page.click_collapse_menu()
    page.click_random_queue()
    page.click("filter_list")
    page.click_on_button_in_zo_screen("Тип")
    assert (
            PikInFilter.expected_types == ServiceRequests(browser).get_type_elements_in_filter()
    ), "Не все значения выпадающего списка присутствуют в Фильтре Тип"


@allure.epic("Тесты UI")
@allure.feature("Пик-листы")
@pytest.mark.smoke
@pytest.mark.parametrize(
    "filter_type, expected_areas",
    [
        ("Технические проблемы", PikInFilter.expected_areas_in_technical_problems),
        ("Претензия", PikInFilter.expected_areas_in_claim),
        ('Консультация', PikInFilter.expected_areas_in_consultation_in_filter),
        ('Услуги', PikInFilter.expected_areas_in_services_in_filter),

    ], ids = ['technical problems', 'claim', 'consultation', 'services']
)
@allure.title("Проверить пик-лист в рандомной очереди в фильтрации - Тип - Область")
def test_check_pick_list_in_filter(browser, login, collapse_menu, filter_type, expected_areas):
    """Проверяем пик-лист в фильтрации для разных типов областей"""

    page = ServiceRequests(browser)
    page.click("Запросы на обслуживание")
    page.click_collapse_menu()
    page.click_random_queue()
    page.click("filter_list")
    page.click_on_button_in_zo_screen("Тип")
    page.click_with_pause(filter_type)
    page.click_on_button_in_zo_screen("Область")
    actual_areas = page.get_type_elements_in_filter()
    assert (
            expected_areas == actual_areas
    ), f"Не все значения в выпадающем списке присутствуют в области типа {filter_type}"


@allure.epic("Тесты UI")
@allure.feature("Пик-листы")
@pytest.mark.smoke
@pytest.mark.parametrize(
    "queue, expected_areas",
    [
        ("Претензии", PikInFilter.expected_areas_in_claim),
        ("Все претензии", PikInFilter.expected_areas_in_claim),
    ], ids = ['claim', 'all claim']
)
@allure.title("Проверить пик-лист в очереди Претензии / Все претензии - области")
def test_check_pick_list_area_in_queue_claim(browser, login, collapse_menu, queue, expected_areas):
    """Проверяем пик-лист в фильтрации - очередь Претензии / Все претензии - области"""

    page = ServiceRequests(browser)
    page.click("Запросы на обслуживание")
    BasePage(browser).pause(5)
    page.click_collapse_menu()
    page.scroll_to(queue)
    page.click_with_pause(queue)
    page.click("filter_list")
    page.click_on_button_in_zo_screen("Область")
    actual_areas = page.get_type_elements_in_filter()
    assert actual_areas == expected_areas,\
        f"Не все значения в выпадающем списке присутствуют в области очереди {queue}"


@allure.epic("Тесты UI")
@allure.feature("Пик-листы")
@pytest.mark.smoke
@pytest.mark.parametrize(
    "filter_type, expected_areas",
    [
        ("Технические проблемы", PikInFilter.expected_areas_in_technical_problems),
        ("Претензия", PikInFilter.expected_areas_in_claim),
        ('Консультация', PikInFilter.expected_areas_in_consultation_in_creating_new_request),
        ('Услуги', PikInFilter.expected_areas_in_services_in_creating_new_request),

    ], ids = ['technical problems', 'claim', 'consultation', 'services']
)
@allure.title("Проверить пик-лист в рандомной очереди в модальном окне 'Создание запроса на обслуживание'")
def test_check_pick_list_in_modal_window(browser, login, collapse_menu, filter_type, expected_areas):
    """Проверяем пик-лист в модальном окне 'Создание запроса на обслуживание'"""

    page = ServiceRequests(browser)
    page.click("Запросы на обслуживание")
    page.click_collapse_menu()
    page.click_random_queue_with_plus_icon()
    page.click("add")
    page.click_on_field_in_modal_window_add_new_service_request("Тип")
    page.click_on_field_in_modal_window_add_new_service_request(filter_type)
    page.click_on_field_in_modal_window_add_new_service_request("Область")
    actual_areas = page.get_type_elements_in_filter()
    assert (
            expected_areas == actual_areas
    ), f"Не все значения в выпадающем списке присутствуют в области типа {filter_type}"


@allure.epic("Тесты UI")
@allure.feature("Пик-листы")
@pytest.mark.smoke
@pytest.mark.parametrize(
    "filter_type, expected_areas",
    [
        ("Технические проблемы", PikInFilter.expected_areas_in_technical_problems),
        ("Претензия", PikInFilter.expected_areas_in_claim),
        ('Консультация', PikInFilter.expected_areas_in_consultation_in_creating_new_request),
        ('Услуги', PikInFilter.expected_areas_in_services_in_creating_new_request),

    ], ids = ['technical problems', 'claim', 'consultation', 'services']
)
@allure.title("Проверить пик-лист в рандомной очереди в запросе на обслуживание ")
def test_check_pick_list_in_zo_card(browser, login, collapse_menu, filter_type, expected_areas):
    """Проверяем пик-лист в запросе на обслуживание"""

    page = ServiceRequests(browser)
    page.click("Запросы на обслуживание")
    page.click_collapse_menu()
    page.click_random_queue_for_pick_list_in_zo_card()
    page.click("Взять в работу следующий")
    page.click_on_button_in_zo_screen("Тип")
    page.click_with_pause(filter_type)
    page.click_on_button_in_zo_screen("Область")
    actual_areas = page.get_type_elements_in_filter()
    assert (
            expected_areas == actual_areas
    ), f"Не все значения в выпадающем списке присутствуют в области типа {filter_type}"