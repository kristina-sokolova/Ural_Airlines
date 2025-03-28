from ui_tests.locators.base_locator import Locator

BUTTON_IN_ZO = Locator(value='//div[contains(@class, "q-field__label") and contains(text(), "{value}")]',
                 name="Кнопка в очереди на экране Запросы на обслуживание")

TYPE_ELEMENTS_IN_FILTER = Locator(value='//div[@class="q-item__label"]',
                 name="Элементы в выпадающем списке")

REQUIRED_FIELD_CREATE_SERVICE_REQUEST = Locator(value='//h3[text()="Создание запроса на обслуживание"]/following::div[text()="{value}"]',
                                        name = "Обязательное поле в модальном окне 'Создание запроса на обслуживание'")
