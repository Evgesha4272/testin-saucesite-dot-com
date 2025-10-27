from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

class CartPage(Base):

    # Locators
    basket_product_name = '//a[@id="item_4_title_link"]'
    basket_product_price = '//div[@class="inventory_item_price"]'
    btn_checkout = '//button[@id="checkout"]'

    # Get elements
    # Get basket product name
    def get_basket_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_product_name)))

    # Get basket product price
    def get_basket_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_product_price)))

    # Get button checkout
    def get_btn_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_checkout)))


    # Methods
    # Method cart standard user
    def check_cart(self):
        self.check_url('https://www.saucedemo.com/cart.html')
        self.get_current_url()
        self.check_word(self.get_basket_product_name(), 'Sauce Labs Backpack')
        self.check_word(self.get_basket_product_price(), '$' + '29.99')
        self.get_btn_checkout().click()
        print('Button checkout clicked.')

    # Method cart standard user
    def check_cart_visual_user(self):
        self.check_url('https://www.saucedemo.com/cart.html')
        self.get_current_url()
        self.get_screenshot()
        self.check_word(self.get_basket_product_name(), 'Sauce Labs Backpack')
        self.check_word(self.get_basket_product_price(), '$' + '29.99')
        self.get_btn_checkout().click()
        print('Button checkout clicked.')

