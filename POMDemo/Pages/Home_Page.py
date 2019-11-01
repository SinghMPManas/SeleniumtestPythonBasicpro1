from selenium.webdriver.common.action_chains import ActionChains
class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

        self.hellouser_menuitem_xpath = "//span[contains(text(),'Hello, Manas')]"
        self.signout_link_xpath = "//span[contains(text(),'Sign Out')]"

    def hover_Signoutmenu(self):
        self.driver.find_element_by_xpath(self.hellouser_menuitem_xpath)
        hover = self.actions.move_to_element(self.hellouser_menuitem_xpath)
        hover.perform()

    def click_signoutlink(self):
        self.driver.find_element_by_xpath(self.signout_link_xpath).click()



