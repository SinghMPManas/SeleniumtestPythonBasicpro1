class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.signin_button_xpath = "//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][contains(text(),'Sign in')]"
        self.username_textbox_id = "ap_email"
        self.continue_button_id = "continue"
        self.password_textbox_id = "ap_password"
        self.login_button = "signInSubmit"

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def click_continue(self):
        self.driver.find_element_by_id(self.continue_button_id).click()

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button).click()
