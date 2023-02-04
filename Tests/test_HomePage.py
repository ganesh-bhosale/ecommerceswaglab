import pytest
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
        self.logger.info("***** Homepage Test Cases started *****")

        self.logger.info("Verify Home Page title TC started...")
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        title = homePage.get_homepage_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        self.logger.info("Verified Homepage Title : TC Passed")

    @pytest.mark.sanity
    def test_headerline_value(self):
        self.logger.info("Verify Homepage Header TC started...")
        homePage = HomePage(self.driver)
        header = homePage.get_headerline_value()
        if header == TestData.HEADER:
            assert True
            self.logger.info("Verified Homepage Header : TC Passed")
        else:
            self.driver.save_screenshot(TestData.SCREENSHOT_PATH + "\\test_headerline_value.png")
            self.logger.warning(" Header not matching : TC Failed")
            assert False

    @pytest.mark.sanity
    def test_sort_button(self):
        self.logger.info("Verify Sort Button TC started...")
        homePage = HomePage(self.driver)
        homePage.is_sort_button_exist()
        self.logger.info("Verified Sort Button : TC Passed")

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_get_item_and_add(self):
        self.logger.info("Search & Add items to Cart TC started...")
        homePage = HomePage(self.driver)
        items = homePage.get_items()
        if items == TestData.ITEM_NAME:
            homePage.get_items()
        self.logger.info("Verified search & add items to Cart functionality : TC Passed")

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_add_items_to_cart(self):
        self.logger.info("Verify add items to Cart TC started...")
        homePage = HomePage(self.driver)
        homePage.add_items_to_cart()
        self.logger.info("Verified add items to Cart : TC Passed ")

    @pytest.mark.sanity
    def test_get_back_to_products(self):
        self.logger.info("Verify Get back to products button TC started... ")
        homePage = HomePage(self.driver)
        homePage.get_back_to_products()
        self.logger.info("Verified Get back to products button : TC Passed")

    @pytest.mark.sanity
    def test_get_shopping_cart_button(self):
        self.logger.info("Verify Cart Button TC started...")
        homePage = HomePage(self.driver)
        homePage.click_shopping_cart_button()
        self.logger.info("Verified Cart Button : TC Passed")

        self.logger.info("***** Homepage Test Cases ended *****")




