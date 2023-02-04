import pytest

from Config.config import TestData
from Pages.CheckoutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from utilities.customLogger import LogGen


class Test_CheckoutPage(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_cart_items(self):
        self.logger.info("***** Checkout Page Test Cases started *****")

        self.logger.info("Verify Cart items button TC started...")
        loginpage = LoginPage(self.driver)
        loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        homepage = HomePage(self.driver)
        homepage.get_items()
        homepage.add_items_to_cart()
        homepage.click_shopping_cart_button()
        checkout = CheckoutPage(self.driver)
        assert checkout.get_cart_items()
        self.logger.info("Verified Cart items button : TC Passed")

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_checkout_button(self):
        self.logger.info("Verify Checkout button TC started...")
        checkout = CheckoutPage(self.driver)
        if checkout.get_cart_items() == True:
            checkout.get_checkout_button()
            self.logger.info("Verified Checkout button :TC Passed")

    @pytest.mark.sanity
    def test_shipping_information(self):
        self.logger.info("Verify Shipping Information Details TC started...")
        checkout = CheckoutPage(self.driver)
        checkout.get_shipping_information()
        checkout.click_continue_button()
        self.logger.info("Verified Shipping Information Details : TC Passed")

    @pytest.mark.sanity
    def test_total_cart_item_value(self):
        self.logger.info("Verify total cart item count TC started...")
        checkout = CheckoutPage(self.driver)
        total_value = checkout.get_item_total_value()
        print("Total items in cart: ", total_value)
        self.logger.info("Verified total items in cart : TC Passed")

    @pytest.mark.sanity
    def test_finish_button(self):
        self.logger.info("Verify Finish button TC started...")
        checkout = CheckoutPage(self.driver)
        checkout.get_finish_button()
        self.logger.info("Verified Finish button : TC Passed")

    @pytest.mark.sanity
    def test_order_confirmation_message(self):
        self.logger.info("Verify Order Confirmation message TC started...")
        checkout = CheckoutPage(self.driver)
        msg = checkout.get_order_confirmation()
        assert msg == TestData.CONFIRM_MSG
        self.logger.info(msg)
        self.logger.info("Verified Order Confirmation message : TC Passed")

        self.logger.info("***** Checkout Page Test Cases ended *****")









