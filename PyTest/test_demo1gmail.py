from selenium import webdriver
import time
import pytest

class TestGmail():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='C:/Users/Sadhana/PycharmProjects/Seleniumtest/Drivers/chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        print(Title + " = Logged into the application successfully")
        driver.quit()

    def test_Gmail_Login(self, test_setup):
        driver.get("https://accounts.google.com/")
        driver.find_element_by_id("identifierId").send_keys("singhmanasmp")
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
        time.sleep(2)
        driver.find_element_by_name("password").send_keys("7thapril:)")
        driver.find_element_by_xpath("//div[@id='passwordNext']//span[@class='CwaK9']").click()
        driver.find_element_by_xpath("//*[@class='gb_Ue']").click()
        driver.find_element_by_xpath("//a[@id='gb23']//span[@class='gb_p']").click()
        time.sleep(2)
        global Title
        Title = driver.title
        assert Title == "Google Account"
        driver.find_element_by_xpath("//span[@class='gb_xa gbii']").click()
        driver.find_element_by_id("gb_71").click()









