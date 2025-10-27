from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

class InfoPage(Base):

    # Locators
    info_page_logo = '//span[@class="title"]'
    input_first_name = '//input[@id="first-name"]'
    input_last_name = '//input[@id="last-name"]'
    input_postal_code = '//input[@id="postal-code"]'
    btn_continue = '//input[@id="continue"]'

    # Variables
    first_name = 'Alex'
    last_name = 'Smith'
    postal_code = '12345'

    # Get elements
    # Get info page logo
    def get_info_page_logo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.info_page_logo)))

    # Get input first name
    def get_input_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_first_name)))

    # Get input last name
    def get_input_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_last_name)))

    # Get input postal code
    def get_input_postal_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_postal_code)))

    # Get button continue
    def get_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_continue)))


    # Methods
    # Method standard user
    def input_info(self):
        self.check_url('https://www.saucedemo.com/checkout-step-one.html')
        self.get_current_url()
        self.check_word(self.get_info_page_logo(), 'Checkout: Your Information')
        self.get_input_first_name().send_keys(self.first_name)
        print('First Name input was entered.')
        self.get_input_last_name().send_keys(self.last_name)
        print('Last Name input was entered.')
        self.get_input_postal_code().send_keys(self.postal_code)
        print('Postal Code input was entered.')
        self.get_btn_continue().click()
        print('Button continue clicked.')

    # Method problem user
    def input_info_problem(self):
        self.check_url('https://www.saucedemo.com/checkout-step-one.html')
        self.get_current_url()
        self.check_word(self.get_info_page_logo(), 'Checkout: Your Information')
        self.get_input_first_name().send_keys(self.first_name)
        print('First Name input was entered.')
        self.get_input_last_name().send_keys(self.last_name)
        print('Last Name input was entered.')
        self.get_input_postal_code().send_keys(self.postal_code)
        print('Postal Code input was entered.')
        self.get_btn_continue().click()
        print('Button continue clicked.')
        self.get_screenshot()

    # Method error user
    def input_info_error(self):
        self.check_url('https://www.saucedemo.com/checkout-step-one.html')
        self.get_current_url()
        self.check_word(self.get_info_page_logo(), 'Checkout: Your Information')
        self.get_input_first_name().send_keys(self.first_name)
        print('First Name input was entered.')
        self.get_input_last_name().send_keys(self.last_name)
        print('Last Name input was entered.')
        self.get_input_postal_code().send_keys(self.postal_code)
        print('Postal Code input was entered.')
        self.get_screenshot()
        self.get_btn_continue().click()
        print('Button continue clicked.')

