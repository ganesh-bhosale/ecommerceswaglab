import pytest
from selenium import webdriver

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from utilities.customLogger import LogGen


class Test_HomePage(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_homepage_title(self):
        self.logger.info("************* Homepage Test Case started **********")
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        title = homePage.get_homepage_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        self.logger.info("************* Homepage Title Case Passed **********")

    @pytest.mark.sanity
    def test_headerline_value(self):
        homePage = HomePage(self.driver)
        header = homePage.get_headerline_value()
        if header == TestData.HEADER:
            assert True
        else:
            self.driver.save_screenshot(TestData.SCREENSHOT_PATH +"\\test_headerline_value.png")
            self.logger.warning(" ***** Test Case failed as Header is not matching *****")
            assert False

    @pytest.mark.sanity
    def test_sort_button(self):
        homePage = HomePage(self.driver)
        homePage.is_sort_button_exist()

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_get_item_and_add(self):
        self.logger.info("***** Search & Add Items to cart Test Case started *****")
        homePage = HomePage(self.driver)
        items = homePage.get_items()
        if items == TestData.ITEM_NAME:
            print(TestData.ITEM_NAME)
            homePage.get_items()
        self.logger.info("***** Test Case Passed *****")

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_add_items_to_cart(self):
        homePage = HomePage(self.driver)
        homePage.add_items_to_cart()

    @pytest.mark.sanity
    def test_get_back_to_products(self):
        homePage = HomePage(self.driver)
        homePage.get_back_to_products()

    @pytest.mark.sanity
    def test_get_shopping_cart_button(self):
        homePage = HomePage(self.driver)
        homePage.click_shopping_cart_button()




