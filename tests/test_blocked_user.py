import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage

@pytest.mark.run(order = 2)
def test_blocked_user(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--incognito')
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    print('\nTest 2 - start.')

    # Call method authorization_block from login_page.py
    login_p = LoginPage(driver)
    login_p.authorization_block()

    driver.quit()

    print('Test 2 - end.')