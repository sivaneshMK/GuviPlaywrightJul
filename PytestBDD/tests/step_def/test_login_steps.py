import pytest
from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage


scenarios("test_login.feature")

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@given("as a user i am on the login page")
def launch_application(get_driver):
    title =get_driver.title
    print(title)

@when("the user enters valid credentials")
def enter_cred(login_page):
    login_page.enter_username("sivanesh")
    login_page.enter_password("password")
    login_page.click_login_button()

@then("the user should be redirected to the dashboard")
def validate_home_page():
    print("we are in home page")