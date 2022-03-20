From selenium



class BasePage():
    def __init__(self, driver, conf= None):

        if conf == None:
            conf = ConfigFile.Config()
        self.conf = conf
        self.driver = driver

    def open(self,url):

    def get_url(self):
        return self.driver.title
