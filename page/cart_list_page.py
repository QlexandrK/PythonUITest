from page.base_page import BasePage


class CartListPage(BasePage):
    FINISH_BUTTON_ON_LINK = '[data-test="finish"]'
    BACK_HOME_BUTTON_ON_LINK = '[data-test=back-to-products]'
    REMOVE_BUTTON_ON_LINK = '[data-test="remove-sauce-labs-backpack"]'
    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'


    def finish_checkout(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON_ON_LINK)


    def checkout_complete(self):
        self.assert_element_is_visible(self.BACK_HOME_BUTTON_ON_LINK)


    def remove_item_in_cart(self):
        self.wait_for_selector_and_click(self.REMOVE_BUTTON_ON_LINK)


    def continue_shopping_button(self):
        self.wait_for_selector_and_click(self.CONTINUE_SHOPPING_BUTTON)
