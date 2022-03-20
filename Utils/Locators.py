from selenium.webdriver.common.by import By

#This class for element on udemy.com page
class MainPage(object):
    home_title = (By.XPATH('//head//title'))
    home_login_button =(By.XPATH("//body/div[2]/div[1]/div[2]/div[6]/a[1]"))

class Login(object):
    login_title_page = (By.ID('auth-to-udemy-title'))
    email_field = (By.CSS_SELECTOR('#email--1'))
    password_field = (By.CSS_SELECTOR('#id_password'))
    login_button = (By.CSS_SELECTOR('#id_password'))

class  home_page(object):
    search_field = (By.CSS_SELECTOR('#u630-search-form-autocomplete--3'))

class search_page(object):
    Title_of_searched = (By.XPATH('//h1'))
    
