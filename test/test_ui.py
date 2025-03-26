from page import cart_list_page
from page.checkout_page import CheckoutPage
from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from page.cart_list_page import CartListPage
from page.checkout_complate_page import CheckoutCompletePage


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    cart_list_page = CartListPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form("John", "Doe", '12345' )
    cart_list_page.finish_checkout()
    checkout_complete_page.checkout_complete()


def test_remove_item(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_list_page = CartListPage(page)


    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    cart_list_page.remove_item_in_cart()
    cart_list_page.continue_shopping_button()



def test_badge_is_visible(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_list_page = CartListPage(page)


    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    cart_list_page.continue_shopping_button()
    inventory_page.assert_badge_is_visible()


def test_product_sort_container(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.product_sort_container()


def test_logout_from_system(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.burger_button_click()
    inventory_page.logout_in_burger()
    login_page.check_is_logout()

