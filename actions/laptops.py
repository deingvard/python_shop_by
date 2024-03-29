import time
import allure
from webium.wait import wait
from pages.base_page_object import BasePageObject
from pages.laptops_page import LaptopsPageLocators
import logging
from webium import BasePage, Finds, Find

LOGGER = logging.getLogger(__name__)


class LaptopsActions(BasePage, BasePageObject):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.laptops_actions = LaptopsPageLocators(driver=self.driver)

    @allure.step('Click show all available laptops')
    def click_show_name_laptops(self):
        LOGGER.info("Click show laptops")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.laptops_actions.show_laptops_name_results)
        self.laptops_actions.show_laptops_name_results.click()

    @allure.step('Define choose_laptop_name() function to set laptops firm checkboxes in list')
    def choose_laptop_name(self, laptop_in_list):
        LOGGER.info("Choose laptop: '%s'", laptop_in_list)
        for section in self.laptops_actions.laptops_name:
            if section.text == laptop_in_list:
                # Scroll to laptops
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           section)
                section.click()
                wait(lambda: len(self.laptops_actions.laptops_name) > 0)
                break

    @allure.step('Set laptop price from minimum to maximum')
    def choose_laptop_price(self, group):
        LOGGER.info("Choose laptop price: min '%s', max '%s' ", group.price_from, group.price_to)
        self.laptops_actions.laptops_price_max_input.send_keys(group.price_to)
        self.laptops_actions.laptops_price_min_input.send_keys(group.price_from)

    @allure.step('Click show all available diagonals')
    def click_show_diagonal(self):
        LOGGER.info("Click show laptops diagonal")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.laptops_actions.show_laptops_diagonal_results)
        self.laptops_actions.show_laptops_diagonal_results.click()

    @allure.step('Set laptops diagonal in list')
    def choose_laptops_diagonal(self, diagonal):

        LOGGER.info("Choose laptop: '%s'", diagonal)
        for section in self.laptops_actions.diagonal_checkbox:
            # Scroll to laptops
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                       section)
            if section.text == diagonal:
                time.sleep(5)
                section.click()
                break
