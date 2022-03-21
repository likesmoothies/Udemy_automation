import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import ConfigFile


class BaseTest(unittest.TestCase):

    def setUp(self):
        Option = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        Option.add_experimental_option("prefs", prefs)
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        Option.add_argument('--no-sandbox')  # # Bypass OS security model
        Option.add_argument("--start-maximized")
        #Option.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
        Option.add_argument('--disable-blink-features=AutomationControlled')
        Option.add_argument("--disable-notifications")
        Option.add_argument('disable-infobars')
        Option.add_argument("--disable-extensions")
        Option.add_experimental_option('excludeSwitches', ['enable-logging'])
        Option.add_experimental_option("excludeSwitches", ["enable-automation"])
        Option.add_experimental_option('useAutomationExtension', True)
        self.conf = ConfigFile.Config()
        self.driver = webdriver.Chrome(executable_path= 'E:/2021/UdemyAutomation/chromedriver.exe',options=Option)
        #self.driver = webdriver.Firefox(GeckoDriverManager().install())
        # self.driver = webdriver.Firefox()

        self.driver.get(self.conf.BASE_URL)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=1).run(suite)
