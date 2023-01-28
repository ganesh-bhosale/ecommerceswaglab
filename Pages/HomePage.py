from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.CheckoutPage import CheckoutPage


class HomePage(BasePage):

    """ Locators """
    HEADER_LINE = (By.CLASS_NAME, "title")
    SORT_BUTTON = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAMES = (By.XPATH, "//a/div[@class='inventory_item_name']")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")
    SHOPPING_CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    """ Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_homepage_title(self, title):
        return self.get_title(title)

    def get_headerline_value(self):
        if self.is_visible(self.HEADER_LINE):
            return self.get_element_text(self.HEADER_LINE)

    def is_sort_button_exist(self):
        if self.is_visible(self.SORT_BUTTON):
            self.do_click(self.SORT_BUTTON)
            return self.is_visible(self.SORT_BUTTON)

    def get_items(self):
        return self.get_element_text(self.ITEM_NAMES)

    def get_items(self):
        self.do_click(self.ITEM_NAMES)

    def add_items_to_cart(self):
        self.do_click(self.ADD_TO_CART)

    def get_back_to_products(self):
        self.do_click(self.BACK_TO_PRODUCTS)

    def click_shopping_cart_button(self):
        self.do_click(self.SHOPPING_CART_BUTTON)
        return CheckoutPage(self.driver)



