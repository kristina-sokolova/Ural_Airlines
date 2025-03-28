from ui_tests.locators.base_locator import Locator

BUTTON = Locator(
    value='//a[text()="{value}"] | //div[text()="{value}"] | //i[text()="{value}"] | //div[contains(@class, "q-item__section")]/div[text()="{value}"] | //button/span[text()="{value}"] | //span[text()="{value}"] | //div[contains(@class, "q-field__label") and text()= "{value}"]/preceding-sibling::div',
    name="Кнопка с видимым текстом")

FIELD = Locator(value='//div[text()="{value}"]/parent::label/preceding-sibling::input',
                name='Поле для ввода')

TITLES = Locator(value='//div[text()="{value}"]',
                 name='Заголовок')

COLLAPSE_MENU = Locator(value='//div[@class="q-focus-helper"]/following::span[@class="v-icon"]',
                        name='Кнопка сворачивания / разворачивания меню')
