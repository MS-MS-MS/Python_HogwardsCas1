from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestTestdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_testdem00(self):
        self.driver.get("https://testerhome.com/")
        sleep(3)