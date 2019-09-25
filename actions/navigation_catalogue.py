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

    def hover_section(self, section_name):
        LOGGER.info("Hover computers section")
        for section in self.navigation_catalog_actions.sections:
            if section.text == section_name:
                section.click()
                wait(lambda: len(self.navigation_catalog_actions.subsections) > 0)
                break

    def hover_sub_section(self, section_name):
        LOGGER.info("Hover laptops section")
        for section in self.navigation_catalog_actions.subsections:
            if section.text == section_name:
                section.click()
                wait(lambda: len(self.navigation_catalog_actions.subsections) > 0)
                break

    def navigate_to(self, section, subsection):
        LOGGER.info("Navigate to %s -> %s", section, subsection)
        self.hover_section(section)
        self.hover_sub_section(subsection)
        self.choose_laptop_in_catalog()

    def choose_laptop_in_catalog(self):
        LOGGER.info("Choose laptops in catalog")
        self.navigation_catalog_actions.choose_laptop.click()
