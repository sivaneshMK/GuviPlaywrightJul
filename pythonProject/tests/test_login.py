from pages.login_page import LoginPage


def test_login_valid_cred(page):
    login_page = LoginPage(page)
    login_page.navigate("https://www.facebook.com")
    login_page.login("sivaneshkirubanandham@gmail.com","abcd!2")
    #assert "Home Page" in login_page.get_tile()
