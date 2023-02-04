import pytest
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class CheckoutPage(BasePage):

    """ Locators """
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout_button")
    INFO_FIRSTNAME = (By.ID, "first-name")
    INFO_LASTNAME = (By.ID, "last-name")
    INFO_POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CLASS_NAME, "submit-button")
    TOTAL_VALUE_TEXT = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.NAME, "finish")
    ORDER_CONFIRM_TEXT = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)


    def get_cart_items(self):
        return self.is_visible(self.CART_ITEM)

    def get_checkout_button(self):
        self.do_click(self.CHECKOUT_BUTTON)

    def get_shipping_information(self):
        self.do_send_keys(self.INFO_FIRSTNAME, TestData.FIRST_NAME)
        self.do_send_keys(self.INFO_LASTNAME, TestData.LAST_NAME)
        self.do_send_keys(self.INFO_POSTAL_CODE, TestData.POSTAL_CODE)

    def click_continue_button(self):
        self.do_click(self.CONTINUE_BUTTON)

    def get_item_total_value(self):
        self.get_element_text(self.TOTAL_VALUE_TEXT)

    def get_finish_button(self):
        self.do_click(self.FINISH_BUTTON)

    def get_order_confirmation(self):
        return self.get_element_text(self.ORDER_CONFIRM_TEXT)