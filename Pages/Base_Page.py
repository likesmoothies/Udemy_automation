import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import ConfigFile



class BasePage(object):
    def __init__(self, driver, conf= None):

        if conf == None:
            conf = ConfigFile.Config()
        self.conf = conf
        self.driver = driver

    #def open(self,url):

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_url(self):
        return self.driver.title

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait(self, type, name):
        if type == 'time':
            time.sleep( name )
        else:
            while not self.driver.find_elements( type, name ):
                time.sleep( 1 )