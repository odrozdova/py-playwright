import re

from playwright.sync_api import Page, expect
from scenarios.models.login import LoginPage


def test_pagetitle(page: Page, get_urls):
    page.goto(get_urls['base_url'])
    #page.goto("https://www.saucedemo.com")

    # Expect title to contain Swag Labs
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_login(page: Page, get_urls):
    page.goto(get_urls['base_url'])
    #page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.login_user(username='standard_user', password='secret_sauce')

    # Expect the URL to have
    expect(page).to_have_url(re.compile(".*inventory"))
