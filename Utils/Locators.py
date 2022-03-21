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
    search_field = (By.CSS_SELECTOR,'#u630-search-form-autocomplete--3')
    profile_hover = (By.XPATH,"//body/div[2]/div[1]/div[2]/div[9]/a[1]/div[1]")

class search_page(object):
    Title_of_searched = (By.XPATH,'//h1')
    
