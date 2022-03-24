from Utils.Locators import  *
from Pages.Base_Page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.element = login_page
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, email):
        self.find_element(*self.element.email_field).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.element.password_field).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.element.login_button).click()
        self.wait("time",5)

    def login(self, username,password):
        #user = users.get_user(user)
        #print(user)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()

    def verifylogo(self):
        logo = self.find_element(*self.element.logo).is_displayed()
        return  logo

    def is_udemy_logged_in(self):
       if (self.find_element(*self.element.login_button).is_displayed()):
            return False
       else:
            return True
