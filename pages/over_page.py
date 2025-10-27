from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

class OverPage(Base):

    # Locators
    field_product_name = '//a[@id="item_4_title_link"]/div'
    field_product_price = '//div[@class="inventory_item_price"]'
    btn_finsh = '//button[@id="finish"]'


    # Get elements
    # Get input username
    def get_field_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_product_name)))

    # Get input password
    def get_field_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_product_price)))

    # Get button login
    def get_btn_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_finsh)))

    # Methods
    def over_check(self):
        self.check_url('https://www.saucedemo.com/checkout-step-two.html')
        self.get_current_url()
        print(self.get_field_product_name().text)
        self.check_word(self.get_field_product_name(), 'Sauce Labs Backpack')
        self.check_word(self.get_field_product_price(), '$' + '29.99')
        self.get_btn_finish().click()
        print('Button is clicked.')