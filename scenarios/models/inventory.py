import os

import yaml


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_btn = page.locator('[id="shopping_cart_container"]')
        self.sort_filter = page.locator('[data-test="product_sort_container"]')
        self.item_containers = page.locator(".inventory_item")
        self.item_labels = page.get_by_role(".inventory_item_name")

    def get_item_containers(self):
        return self.item_containers

    def read_inventory_labels(self):
        with open(f'./yaml/inventory.yaml') as file_read:
            file = yaml.load(file_read, Loader=yaml.FullLoader)

        inv_labels = []
        for label in file['item_desc']:
            inv_labels.append(label)
        return inv_labels

    def get_inventory_labels(self):
        page_labels = self.item_labels
        label_list = []
        for label in page_labels:
            label_list.append(label.text)
        return label_list

