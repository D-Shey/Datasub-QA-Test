import pytest
from playwright.sync_api import Page, expect


@pytest.mark.form
def test_form(page: Page) -> None:

    page.goto("https://qatest.datasub.com/")
    # time.sleep(5)
    page.locator(".col-lg-5 > .bg-primary").scroll_into_view_if_needed()
    page.locator(".col-lg-5 > .bg-primary").click()
    page.get_by_role("textbox", name="Your Name").click()
    page.get_by_role("textbox", name="Your Name").fill("Denis")
    page.locator("#email").click()
    page.locator("#email").fill("1234@gmail.com")
    page.locator("#service").select_option("B Service")
    page.get_by_role("radio", name="Business").check()
    page.get_by_role("checkbox", name="Cash").check()
    page.get_by_role("textbox", name="Message").click()
    page.get_by_role("textbox", name="Message").fill("test1234")
    page.on("request", lambda request: print(f"➡ Запрос: {request.method} {request.url}"))
    page.on("response", lambda response: print(f"⬅ Ответ: {response.status} {response.url}"))

    with page.expect_response("https://example.com/api/subscribe") as response_info:
        page.get_by_role("button", name="Request A Quote").click()

    def log_request(request):
        print(f"Request URL: {request.url}")

    page.on("request", log_request)
    response = response_info.value
    print(f"Ответ пришёл с URL: {response.url}")
    print(f"Статус ответа: {response.status}")

    assert response.status == 200, f"Ошибка статус код: {response.status}"

    try:
        expect(page.get_by_role("button", name="Request A Quote")).to_be_visible()
    except:
        assert False, "Кнопка 'Request A Quote' не найдена"
