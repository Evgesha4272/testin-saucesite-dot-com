import datetime

class Base:

    # Initialization class instance
    def __init__(self, driver):
        self.driver = driver

    # Methods to get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url is: {get_url}')

    # Method to assert url
    def check_url(self, check_url):
        get_url = self.driver.current_url
        assert get_url == check_url
        print('We are on page. Url is same.')

    # Method to assert element on the page
    def check_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Same. Verification completed.')

    # Method to check error message
    def check_message(self, word, result):
        value_word = word.text
        assert value_word == result
        print('We have error message.')

    # Method to make screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name_screenshot = f'screenshot_{now_date}.png'
        self.driver.save_screenshot('B:\\PyCharm Projects\\TestSiteSauceDitComm\\screens\\' + name_screenshot)
        print('Screenshot saved.')




