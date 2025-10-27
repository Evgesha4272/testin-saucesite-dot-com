import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.over_page import OverPage

@pytest.mark.run(order = 1)
def test_correct_user(set_up):

    # Setting browser for start
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--incognito')
    g = Service()
    driver = webdriver.Chrome(options = options, service = g)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    print('\nTest 1 - start.')

    # Call method authorization from login_page.py
    login_p = LoginPage(driver)
    login_p.authorization()

    # Call method chose_product from main_page.py
    main_p = MainPage(driver)
    main_p.chose_product()

    # Call method check_cart from cart_page.py
    cart_p = CartPage(driver)
    cart_p.check_cart()

    # Call method input_info from info_page.py
    info_p = InfoPage(driver)
    info_p.input_info()

    # Call method over_check from over_page.py
    over_p = OverPage(driver)
    over_p.over_check()

    driver.quit()

    print('Test 1 - end.')
