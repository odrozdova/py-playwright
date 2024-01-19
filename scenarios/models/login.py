import os


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('[placeholder="Username"]')
        self.password_input = page.locator('[placeholder="Password"]')
        self.login_btn = page.locator('[id="login-button"]')

    def input_username(self):
        self.username_input.fill(os.getenv("USERNAME"))

    def input_password(self):
        self.password_input.fill(os.getenv("PASS"))

    def click_login_btn(self):
        self.login_btn.click()

    def login_user(self):
        self.input_username()
        self.input_password()
        self.click_login_btn()

