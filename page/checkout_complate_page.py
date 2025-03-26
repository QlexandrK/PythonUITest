from page.base_page import BasePage


class CheckoutCompletePage(BasePage):
    BACK_HOME_BUTTON_ON_LINK = '[data-test="back-to-products"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-complete.html'

    def checkout_complete(self):
        self.assert_element_is_visible(self.BACK_HOME_BUTTON_ON_LINK)
