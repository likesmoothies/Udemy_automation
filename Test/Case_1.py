import unittest
from Test.Base_Test import BaseTest
from Pages.Login_Page import *
from Pages.Seach_Page import *
#from Pages.Seach_Page import

class e2e_case(BaseTest):

    def test_page_load(self):
        login = LoginPage(self.driver)
        #if login.is_udemy_logged_in():
         #   print("already login")
        login.enter_email(self.conf.USERNAME)
        login.enter_password(self.conf.PASSWORD)
        login.click_login_button()
        search = SearchPage(self.driver)
        search.Search_Course("Selenium Webdriver")

        #print(str(login.verifylogo()))
        #self.assertTrue(login.verifylogo())

   # def test_search_course(self):




        #page = Main_page(self.driver)
        #self.assertTrue(page.check_load_page())
        #self.assertEqual(page.check_title(),"Kursus Online - Pelajari Apa Pun Sesuai Jadwal Anda | Udemy")

     #def clickbuttonlogin(self):
        #page = Main_page(self.driver)
       # page.Click_Login_Button()
        #self.assertTrue("test")

