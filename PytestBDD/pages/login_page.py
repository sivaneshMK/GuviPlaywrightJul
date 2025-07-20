from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_txt_bx = (By.NAME, "email")
        self.password_txt_bx = (By.NAME, 'pass')
        self.login_btn = (By.NAME, 'login')

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt_bx).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt_bx).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()
