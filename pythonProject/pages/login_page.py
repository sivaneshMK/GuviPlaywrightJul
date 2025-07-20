from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.user_input_txt_box = page.locator("input#email")
        self.password_input_txt_box = page.locator("input#pass")
        self.login_btn = page.locator("//button[@name = 'login']")


    def login(self, username, password):
        self.user_input_txt_box.fill(username)
        self.password_input_txt_box.fill("abcd!2")
        self.login_btn.click()