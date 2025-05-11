from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Для визуальной проверки языка
    import time
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button is not None, "Add to basket button is not found"