import pytest
from selenium import webdriver

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from utilities import customLogger
from utilities.customLogger import LogGen


class Test_Login(BaseTest):

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_loginPage_tile(self):
        self.logger.info("***** Verifying Login Page Title *****")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_loginPage_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        self.logger.info("***** Test Case passed *****")

    @pytest.mark.sanity
    def test_loginButton(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_loginbutton_exist()
        assert flag

    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        self.logger.info("***** Login Page Test Cases Ended *****")



