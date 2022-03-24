from Utils.Locators import  *
from Pages.Base_Page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.element = search_page
        super(SearchPage, self).__init__(driver)

    def Search_Course(self,Course):
        self.find_element(*self.element.search_field).send_keys(Course)
        self.find_element(*self.element.button_search.click())

    def Verify_Title_Course(self):
        Title = self.find_element(*self.element.Title_of_searched).text
        return  Title

    def Choose_Course(self):
         self.find_element(*self.element.Choose_The_Course).click()
