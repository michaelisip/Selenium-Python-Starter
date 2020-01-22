from selenium import webdriver

class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://google.com')

Test()