import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.run(order = 3)
def test_problem_user(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--incognito')
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    print('\nTest 3 - start.')

    # # Call method authorization_problem from login_page.py
    login_p = LoginPage(driver)
    login_p.authorization_problem()

    # Call method chose_product from main_page.py
    main_p = MainPage(driver)
    main_p.chose_product()

    # Call method check_cart from cart_page.py
    cart_p = CartPage(driver)
    cart_p.check_cart()

    # Call method input_info from info_page.py
    info_p = InfoPage(driver)
    info_p.input_info_problem()

    driver.quit()

    print('Test 3 - end.')