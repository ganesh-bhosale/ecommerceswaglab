from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPageDDT(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    login_button = (By.ID, "submit")
    logout_button = (By.CLASS_NAME, "wp-block-button__link")

    """Constructor of Page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_DDT_URL)
        self.driver.maximize_window()

    def do_loginDDT(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.login_button)

    def do_logout(self):
        self.do_click(self.logout_button)









