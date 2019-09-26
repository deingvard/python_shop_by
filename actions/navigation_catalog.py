import allure

from pages.base_page_object import BasePageObject
from pages.navigation_catalog_page import NavigationCatalogPageLocators
import logging
from webium.wait import wait
from webium import BasePage, Finds, Find

LOGGER = logging.getLogger(__name__)


class NavigationCatalogActions(BasePage, BasePageObject):

    # Get an instance driver, app, NavigationCatalogPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_catalog_actions = NavigationCatalogPageLocators(driver=self.driver)

    @allure.step('Click on the section "Computers" on the main page')
    def click_catalog_section(self, section_name):
        LOGGER.info("Hover computers section")
        for section in self.navigation_catalog_actions.sections:
            if section.text == section_name:
                section.click()
                wait(lambda: len(self.navigation_catalog_actions.subsections) > 0)
                break

    @allure.step("Navigate to 'Computers' and select 'Laptops'.")
    def navigate_to(self, section_computers, subsection_notebooks):
        LOGGER.info("Navigate to %s -> %s", section_computers, subsection_notebooks)
        self.click_catalog_section(section_computers)
        self.choose_laptop_in_catalog()

    # Click on the "Laptops" button on the catalog page
    def choose_laptop_in_catalog(self):
        LOGGER.info("Choose laptops in catalog")
        self.navigation_catalog_actions.choose_laptop.click()
