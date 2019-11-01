from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Sadhana/PycharmProjects/Seleniumtest/Drivers/chromedriver.exe')
        cls.driver.maximize_window()

    def test_AmazonLogin_Validation(self):
        driver = self.driver
        driver.get("https://www.amazon.in/")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][contains(text(),'Sign in')]").click()
        driver.find_element_by_id("ap_email").send_keys("7411524194")
        driver.find_element_by_id("continue").click()
        driver.find_element_by_id("ap_password").send_keys("7thapril:)")
        driver.find_element_by_id("signInSubmit").click()
        time.sleep(2)
        signoutelement = driver.find_element_by_xpath("//span[contains(text(),'Hello, Manas')]")
        actionhover = ActionChains(driver).move_to_element(signoutelement)
        actionhover.perform()
        driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        time.sleep(2)
        print("Testing Completed")

if __name__ == '__main__':
    unittest.main()





