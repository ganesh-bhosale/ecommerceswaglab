from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """ By Locators"""
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LEFT_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    """Constructor of Page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_loginPage_title(self, title):
        return self.get_title(title)

    def is_loginbutton_exist(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def get_url(self, url):
        return self.get_current_url(url)

    def do_logout(self):
        self.do_click(self.LEFT_MENU)
        self.do_click(self.LOGOUT_BUTTON)
