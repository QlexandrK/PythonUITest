from page.base_page import BasePage


class CartListPage(BasePage):
    FINISH_BUTTON_ON_LINK = '[data-test="finish"]'
    BACK_HOME_BUTTON_ON_LINK = '[data-test=back-to-products]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'


    def finish_checkout(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON_ON_LINK)


    def checkout_complete(self):
        self.assert_element_is_visible(self.BACK_HOME_BUTTON_ON_LINK)
