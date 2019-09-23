import time

from webium.wait import wait
from pages.laptops_page import LaptopsPageLocators
import pytest
import logging
from webium import BasePage, Finds, Find

LOGGER = logging.getLogger(__name__)


class LaptopsActions(BasePage):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.laptops_actions = LaptopsPageLocators(driver=self.driver)

    # Enter username, string value
    def choose_laptop_name(self, laptop_in_list):
        LOGGER.info("Choose laptop: '%s'", laptop_in_list)
        for section in self.laptops_actions.laptops_name:
            if section.text == laptop_in_list:
                section.click()
                wait(lambda: len(self.laptops_actions.laptops_name) > 0)
                break

    # Enter username, string value
    def choose_laptop_price(self, min_price, max_price):
        LOGGER.info("Choose laptop price: min '%s', max '%s' ", min_price, max_price)
        self.laptops_actions.laptops_price_max_input.send_keys(max_price)
        self.laptops_actions.laptops_price_min_input.send_keys(min_price)

    def choose_laptops_diagonal(self, from_laptops_diagonal, to_laptops_diagonal):
        LOGGER.info("Choose laptop diagonal: min '%s', max '%s' ", from_laptops_diagonal, to_laptops_diagonal)
        self.laptops_actions.laptops_diagonal_min_checkbox.send_keys(from_laptops_diagonal)
        self.laptops_actions.laptops_diagonal_max_checkbox.send_keys(to_laptops_diagonal)

    def click_show_diagonal(self):
        LOGGER.info("Click show laptops diagonal")
        self.laptops_actions.is_element_present('show_laptops_diagonal_results')
        print("CCCCC")
        # ddd.click()
        # kkk.click()
        # self.laptops_actions.show_laptops_diagonal_results.click()
