import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(10)  # Для проверяющего человека
    assert is_element_present(browser) == True, "Корзина не найдена"


def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        return True
    except:
        return False
