import pytest
from playwright.sync_api import Page, expect

@pytest.mark.register
def test_example(page: Page) -> None:
    page.goto("https://radar-analytica.ru/")
    expect(page.get_by_role("link", name="Регистрация")).to_be_visible()
    page.get_by_role("link", name="Регистрация").click()

    try:
        expect(page.get_by_role("button", name="Зарегистрироваться")).to_be_visible()
    except:
        assert False, "Кнопка Зарегистрироваться не найдена"

