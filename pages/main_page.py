from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

class MainPage(Base):

    # Locators
    select_filter = '//select[@class="product_sort_container"]'
    btn_add_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    btn_cart = '//a[@class="shopping_cart_link"]'
    btn_burger = '//button[@id="react-burger-menu-btn"]'
    btn_cross = '//button[@id="react-burger-cross-btn"]'
    logo_site = '//span[@class="title"]'

    # Get elements
    # Get logo site
    def get_logo_site(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo_site)))

    # Get select filter
    def get_select_filter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_filter)))

    # Get button burger
    def get_btn_burger(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_burger)))

    # Get button cross
    def get_btn_cross(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_cross)))

    # Get logo page
    def get_logo_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo_site)))

    # Get button product 1
    def get_btn_add_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_add_product_1)))

    # Get button cart
    def get_btn_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_cart)))


    # Methods
    # Method chose product standard user
    def chose_product(self):
        self.check_url('https://www.saucedemo.com/inventory.html')
        self.get_current_url()
        self.check_word(self.get_logo_page(), 'Products')
        self.get_select_filter().click()
        print('Select filter is pressed.')
        self.get_select_filter().send_keys(Keys.DOWN + Keys.ENTER)
        print('Filters selected.')
        self.get_btn_burger().click()
        print('Button burger pressed.')
        self.get_btn_cross().click()
        print('Burger menu closed.')
        self.get_btn_add_product_1().click()
        print('Product one was added.')
        self.get_btn_cart().click()
        print('Button cart pressed.')

    # Method product error user
    def chose_product_error_user(self):
        self.check_url('https://www.saucedemo.com/inventory.html')
        self.get_current_url()
        self.check_word(self.get_logo_page(), 'Products')
        self.get_btn_burger().click()
        print('Button burger pressed.')
        self.get_btn_cross().click()
        print('Burger menu closed.')
        self.get_btn_add_product_1().click()
        print('Product one was added.')
        self.get_btn_cart().click()
        print('Button cart pressed.')

    # Method product error user
    def chose_product_visual_user(self):
        self.check_url('https://www.saucedemo.com/inventory.html')
        self.get_current_url()
        self.check_word(self.get_logo_page(), 'Products')
        self.get_btn_burger().click()
        print('Button burger pressed.')
        self.get_btn_cross().click()
        print('Burger menu closed.')
        self.get_btn_add_product_1().click()
        print('Product one was added.')
        self.get_btn_cart().click()
        print('Button cart pressed.')
        self.get_screenshot()
