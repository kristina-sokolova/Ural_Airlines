from ui_tests.pages.base_page import BasePage
from ui_tests.locators import general_locators


class DashboardsPage(BasePage):

    def title_dashboard_is_visible(self):
        return self.is_visible(general_locators.TITLES.format(value="Дашборды"))
