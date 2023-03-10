import time
import pytest
from Config.config import TestData
from Pages.LoginPageDDT import LoginPageDDT
from Tests.test_Base import BaseTest
from utilities import XLUtils
from utilities.customLogger import LogGen


class Test_Login(BaseTest):

    logger = LogGen.loggen()
    file = TestData.LOGINDATA_FILENAME
    sheetName = TestData.LOGINDATA_SHEETNAME

    @pytest.mark.regression
    def test_login_ddt(self):

        self.logger.info("***** Starting Data Driven Test Case *****")

        self.logger.info("Verify Login Page DDT TC started...")
        self.loginPageDDT = LoginPageDDT(self.driver)

        self.rows = XLUtils.getRowCount(self.file, self.sheetName)
        status_lst = []

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.file, self.sheetName, r, 1)
            self.password = XLUtils.readData(self.file, self.sheetName, r, 2)
            self.expected = XLUtils.readData(self.file, self.sheetName, r, 3)

            self.loginPageDDT.do_loginDDT(self.username, self.password)
            time.sleep(10)

            """ Use page title to verify """
            act_title = self.driver.title
            exp_title = TestData.LOGIN_DDT_TITLE

            """ Use page URL to verify """
            # act_url = self.driver.current_url
            # exp_url = TestData.LOGGED_IN_URL

            if act_title == exp_title :
                if self.expected == 'pass':
                    self.logger.info("passed")
                    self.loginPageDDT.do_logout()
                    status_lst.append("Pass")

                elif self.expected == 'fail':
                    self.logger.info("failed")
                    self.loginPageDDT.do_logout()
                    status_lst.append("Fail")

            elif act_title != exp_title :
                if self.expected == 'pass':
                    self.logger.info("failed")
                    status_lst.append("Fail")

                elif self.expected == 'fail':
                    self.logger.info("passed")
                    status_lst.append("Pass")

                print(status_lst)

        if "Fail" not in status_lst:
            self.logger.info("Verified Login DDT successfully : TC Passed")
            assert True

        else:
            self.logger.error("Login DDT Failed : TC Failed")
            assert False

        self.logger.info("***** Data Driver Test Cases Completed *****")













