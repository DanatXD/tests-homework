import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_yandex_login_page_opens(browser):
    browser.get("https://passport.yandex.ru/auth/")
    assert "Яндекс" in browser.title or "Авторизация" in browser.title


def test_yandex_login_empty_fields(browser):
    browser.get("https://passport.yandex.ru/auth/")
    login_field = browser.find_element(By.ID, "passp-field-login")
    login_field.send_keys(Keys.ENTER)
    assert "passp-field-login" in browser.page_source or "Введите" in browser.page_source


def test_yandex_login_invalid_user(browser):
    browser.get("https://passport.yandex.ru/auth/")
    login_field = browser.find_element(By.ID, "passp-field-login")
    login_field.send_keys("nonexistent_user_123456789")
    login_field.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)
    assert "Такого аккаунта нет" in browser.page_source or "не найден" in browser.page_source