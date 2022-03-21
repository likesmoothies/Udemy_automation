import unittest
from Test.Base_Test import BaseTest
from Pages.Login_Page import *
#from Pages.Seach_Page import

class e2e_case(BaseTest):
    #self.login = LoginPage(self.driver)

    def test_page_load(self):
        login = LoginPage(self.driver)
        login.enter_email(self.conf.USERNAME)
        login.enter_password(self.conf.PASSWORD)
        login.click_login_button()
        print(login.verifylogo())
        self.assertTrue(login.verifylogo())


        #page = Main_page(self.driver)
        #self.assertTrue(page.check_load_page())
        #self.assertEqual(page.check_title(),"Kursus Online - Pelajari Apa Pun Sesuai Jadwal Anda | Udemy")

  #  def clickbuttonlogin(self):
        #page = Main_page(self.driver)
       # page.Click_Login_Button()
        #self.assertTrue("test")

