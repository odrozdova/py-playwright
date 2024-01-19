import pytest
import yaml
from playwright.sync_api import Page

from scenarios.models.login import LoginPage
from scenarios.models.menu import Menu


@pytest.fixture
def do_login(page: Page, get_urls):
    page.goto(get_urls['base_url'])
    login_page = LoginPage(page)
    yield login_page.login_user()
    menu = Menu(page)
    menu.logout_from_menu()
