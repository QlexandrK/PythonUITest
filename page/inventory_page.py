from page.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR = ".inventory_item >> text='Add to cart'"
    ADD_TO_CART_BIKE_LIGHT = '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ADD_TO_CART_TSHIRT = '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
    SHOPPING_CART_LINK_SELECTOR = '[data-test="shopping-cart-link"]'
    SHOPPING_CART_BADGE = '[data-test="shopping-cart-badge"]'
    PRODUCT_SORT_CONTAINER = '[data-test="product-sort-container"]'
    BURGER_BUTTON = '.bm-burger-button'
    LODOUT_BOTTON = '[data-test="logout-sidebar-link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        # self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def shopping_cart_link_button(self):
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def add_to_cart_bike_light(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_BIKE_LIGHT)

    def add_to_cart_tshirt(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_TSHIRT)

    def assert_badge_is_visible(self):
        self.assert_element_is_visible(self.SHOPPING_CART_BADGE)

    def product_sort_container(self, value):
        self.wait_for_selector_and_click(self.PRODUCT_SORT_CONTAINER)
        self.select_options(self.PRODUCT_SORT_CONTAINER, value)

    def burger_button_click(self):
        self.wait_for_selector_and_click(self.BURGER_BUTTON)

    def logout_in_burger(self):
        self.wait_for_selector_and_click(self.LODOUT_BOTTON)

