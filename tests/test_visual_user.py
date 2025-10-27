import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.over_page import OverPage

@pytest.mark.run(order = 5)
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

    print('\nTest 5 - start.')

    # Call method authorization_visual from login_page.py
    login_p = LoginPage(driver)
    login_p.authorization_visual()

    # Call method chose_product_visual_user from main_page.py
    main_p = MainPage(driver)
    main_p.chose_product_visual_user()

    # Call method check_cart_visual_user from cart_page.py
    cart_p = CartPage(driver)
    cart_p.check_cart_visual_user()

    # Call method input_info from info_page.py
    info_p = InfoPage(driver)
    info_p.input_info()

    # Call method over_check from over_page.py
    over_p = OverPage(driver)
    over_p.over_check()

    driver.quit()

    print('Test 5 - end.')
