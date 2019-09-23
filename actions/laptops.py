#parameter_laptop

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
    def click_lenovo(self):
        LOGGER.info("Click Lenovo")
        self.laptops_actions.parameter_laptop.click()
