from ui_tests.pages.dashboards_page import DashboardsPage
import allure
import pytest



@allure.epic("Тесты UI")
@allure.feature("Страница 'Дашборды'")
@allure.title("Проверить отображение названия 'Дашборды'")
@pytest.mark.regression
def test_title_dashboard_is_visible(browser, login):
    """Проверяем, что отображено название 'Дашборды'"""
    assert DashboardsPage(browser).title_dashboard_is_visible()
