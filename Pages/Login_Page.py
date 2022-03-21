from Utils.Locators import  *
from Pages.Base_Page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.login_page = login_page
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, email):
        self.find_element(*self.login_page.email_field).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.login_page.password_field).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.login_page.login_button).click()
        self.wait("time",3)

    def login(self, username,password):
        #user = users.get_user(user)
        #print(user)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()


    def login_with_valid_user(self, user):
        self.login(user)
        return True

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text

    def verifylogo(self):
        logo = self.find_element(*self.login_page.logo).is_displayed()
        return  logo
