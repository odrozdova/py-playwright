class Menu:
    def __init__(self, page):
        self.page = page
        self.menu_btn = page.locator('[id="react-burger-menu-btn"]')
        self.logout_btn = page.locator('[id="logout_sidebar_link"]')
        self.all_items_btn = page.locator('[id="inventory_sidebar_link"]')
        self.about_btn = page.locator('[id="about_sidebar_link"]')
        self.reset_app_btn = page.locator('[id="reset_sidebar_link"]')

    def logout_from_menu(self):
        self.menu_btn.click()
        self.logout_btn.click()
