from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base

class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    input_user_name = '//input[@id="user-name"]'
    input_password = '//input[@id="password"]'
    btn_login = '//input[@id="login-button"]'
    # Blocked user
    error_message = '//h3[@data-test="error"]'


    # Variables
    # Normal user
    username = 'standard_user'
    password = 'secret_sauce'

    # Block user
    username_block = 'locked_out_user'
    error_message_block = 'Epic sadface: Sorry, this user has been locked out.'

    # Problem user
    username_problem = 'problem_user'

    # Error user
    username_error = 'error_user'

    # Error user
    username_visual = 'visual_user'

    # Get elements
    # Get input username
    def get_input_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_user_name)))

    # Get input password
    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    # Get button login
    def get_btn_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_login)))

    # Get error message
    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.error_message)))


    # Methods
    # Method for standard user
    def authorization(self):
        self.get_current_url()
        self.get_input_user_name().send_keys(self.username)
        print('Input login is entered.')
        self.get_input_password().send_keys(self.password)
        print('Input password is entered.')
        self.get_btn_login().click()
        print('Button is clicked.')

    # Method for blocked user
    def authorization_block(self):
        self.get_current_url()
        self.get_input_user_name().send_keys(self.username_block)
        print('Input login is entered.')
        self.get_input_password().send_keys(self.password)
        print('Input password is entered.')
        self.get_btn_login().click()
        print('Button is clicked.')
        self.check_message(self.get_error_message(), self.error_message_block)

    # Method for problem user
    def authorization_problem(self):
        self.get_current_url()
        self.get_input_user_name().send_keys(self.username_problem)
        print('Input login is entered.')
        self.get_input_password().send_keys(self.password)
        print('Input password is entered.')
        self.get_btn_login().click()
        print('Button is clicked.')
        self.get_screenshot()

    # Method for error user
    def authorization_error(self):
        self.get_current_url()
        self.get_input_user_name().send_keys(self.username_error)
        print('Input login is entered.')
        self.get_input_password().send_keys(self.password)
        print('Input password is entered.')
        self.get_btn_login().click()
        print('Button is clicked.')

    # Method for visual user
    def authorization_visual(self):
        self.get_current_url()
        self.get_input_user_name().send_keys(self.username_visual)
        print('Input login is entered.')
        self.get_input_password().send_keys(self.password)
        print('Input password is entered.')
        self.get_btn_login().click()
        print('Button is clicked.')
        self.get_screenshot()

