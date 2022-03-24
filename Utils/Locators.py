from selenium.webdriver.common.by import By

#This class for element on udemy.com page
class main_page_locator(object):
    home_title = (By.XPATH,'//head//title')
    main_login_button = (By.XPATH,"//body/div[2]/div[1]/div[2]/div[6]/a[1]")
    logo = (By.XPATH,"//a[@href='/']//img[@alt='Udemy']")


class login_page(object):
    login_title_page = (By.ID,'auth-to-udemy-title')
    email_field = (By.CSS_SELECTOR,'#email--1')
    password_field = (By.CSS_SELECTOR,'#id_password')
    login_button = (By.XPATH,"//input[@id='submit-id-submit']")
    logo = (By.CSS_SELECTOR,'#u293-popper-trigger--19')

class  home_page(object):

    profile_hover = (By.XPATH,"//body/div[2]/div[1]/div[2]/div[9]/a[1]/div[1]")

class search_page(object):
    Title_of_searched = (By.XPATH,'//h1')
    Choose_The_Course = (By.XPATH,"//div[@id='u306-popper-trigger--133']")
    search_field = (By.CSS_SELECTOR, "//form//*[@name='q']")
    button_search = (By.XPATH,"//button[@type='submit']")

class course_detail_page(object):
    Title_of_the_course = (By.XPATH,"//h1")
#    Buy_Button = (By.)
    
