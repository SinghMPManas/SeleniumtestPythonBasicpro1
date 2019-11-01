from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.Login_Page import LoginPage
# from POMDemo.Pages.Home_Page import HomePage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Sadhana/PycharmProjects/Seleniumtest/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(3)

    def test_Login_Validation(self):
        driver = self.driver
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        login = LoginPage(driver)
        login.click_signin()
        login.enter_username("7411524194")
        login.click_continue()
        login.enter_password("7thapril:)")
        login.click_login()
        time.sleep(2)
        # home = HomePage(driver)
        # home.hover_Signoutmenu()
        # home.click_signoutlink()
        # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Login Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Sadhana/PycharmProjects/Seleniumtest/Reports'))
