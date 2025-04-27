
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            # отключаем CORS
            args = ["--disable-web-security", "--disable-features=IsolateOrigins,site-per-process"]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


