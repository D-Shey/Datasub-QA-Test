import pytest
from playwright.sync_api import Page

invalid_emails = [
    "",
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@",
    "username@com",
    "username@.com.",
    "username@com.",
    "username@-com.com",
    "username@com..com",
    "user name@domain.com",
    "username@domain..com",
    "user@domain@domain.com",
    "username@.domain.com",
    "username@domain.com (Smith)",
    "username@domain",
     "фывыфвф@gmail.com"
]

@pytest.mark.parametrize("invalid_email", invalid_emails)
def test_email_validation_negative(page: Page, invalid_email: str) -> None:
    page.goto("https://qatest.datasub.com/")
    page.locator(".col-lg-5 > .bg-primary").scroll_into_view_if_needed()

    requests_sent = []
    def capture_request(request):
        if "/api/" in request.url:
            requests_sent.append(request.url)
    page.on("request", capture_request)
    page.get_by_role("textbox", name="Your Name").fill("Denis")
    page.locator("#email").fill(invalid_email)
    page.locator("#service").select_option("B Service")
    page.get_by_role("textbox", name="Message").fill("test1234")
    page.get_by_role("button", name="Request A Quote").click()
    page.wait_for_timeout(3000)

    if requests_sent:
        pytest.fail(f" С невалидным email {invalid_email} ушли запросы: {requests_sent}")
    else:
        print(f" С невалидным email {invalid_email} запросы не ушли, всё ок.")
