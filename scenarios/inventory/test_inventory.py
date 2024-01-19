import re

from playwright.sync_api import Page, expect
from scenarios.models.inventory import InventoryPage


def test_inventory_count(page: Page, do_login):
    inv_page = InventoryPage(page)
    expect(inv_page.get_item_containers()).to_have_count(6)


def test_inventory_labels(page: Page):
    inv_page = InventoryPage(page)
    expected_labels = inv_page.read_inventory_labels()
    page_labels = inv_page.get_inventory_labels()
    expect(page_labels).to_have_text(expected_labels)
