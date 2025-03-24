from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=1000)
page = browser.new_page()
page.goto('https://www.saucedemo.com/')

inventory_item = ".inventory_item >> text='Add to cart'"

page.type(selector='[id="user-name"]', text='standard_user')
page.fill(selector='#password', value='secret_sauce')
page.click(selector='.submit-button')
page.click(selector='#add-to-cart-sauce-labs-backpack')
page.click(selector='.shopping_cart_link')
page.is_visible(inventory_item)
button_checkout = '#checkout'
page.is_visible(button_checkout)
page.click(button_checkout)
page.type(selector='#first-name', text='Vasya')
page.type(selector='[id="last-name"]', text='Pupkins')
page.type(selector='[id="postal-code"]', text='Blyat')
page.click(selector='#continue')
page.click(selector='#finish')
page.click(selector='#back-to-products')

# page.wait_for_url('https://www.saucedemo.com/inventory.html', time=10000)
# page.wait_for_selector('#inventory_container')

browser.close()
playwright.stop()