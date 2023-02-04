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
        self.logger.info("***** Login Page Test Cases started *****")

        self.logger.info("Verify Login Page Title TC started...")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_loginPage_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        self.logger.info("Login Page Title Verified : TC Passed")

    @pytest.mark.sanity
    def test_loginButton(self):
        self.logger.info("Verify Login Button TC started...")
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_loginbutton_exist()
        assert flag
        self.logger.info("Login Page Button Verified : TC Passed")


    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("Verify User Login TC started...")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.logger.info("User Logged in successfully : TC PASSED")

        self.logger.info("***** Login Page Test Cases Ended *****")



