from Pages.Base_Page import BasePage
from Utils.Locators import *

class Main_page(BasePage):
    def __init__(self, driver):
        super(Main_page, self).__init__(driver)
        #self.mainpage = main_page_locator
        self.loginbutton = ("//body/div[2]/div[1]/div[2]/div[6]/a[1]")

    def check_load_page(self):
        self.find_element(*self.mainpage.logo)

    def Click_Login_Button(self):
        self.find_element('xpath',self.loginbutton).click()

    def check_title(self):
        Title = self.find_element(*self.mainpage.home_title).text()
        return Title
