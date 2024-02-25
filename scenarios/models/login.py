import os


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('[placeholder="Username"]')
        self.password_input = page.locator('[placeholder="Password"]')
        self.login_btn = page.locator('[id="login-button"]')

    def input_username(self, username):
        self.username_input.fill(username)

    def input_password(self, password):
        self.password_input.fill(password)

    def click_login_btn(self):
        self.login_btn.click()

    def login_user(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

