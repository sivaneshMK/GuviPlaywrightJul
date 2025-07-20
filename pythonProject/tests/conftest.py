import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def setup():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(permissions=[])
    page = context.new_page()
    yield page
    context.close()
