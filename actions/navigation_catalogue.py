from pages.navigation_catalog_page import NavigationCatalogPageLocators
import logging
from selenium.webdriver import ActionChains
from webium.wait import wait
from webium import BasePage, Finds, Find
from selenium.webdriver.common.by import By
LOGGER = logging.getLogger(__name__)


class NavigationCatalogActions(BasePage):

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
        self.hover_section(section)
        self.hover_sub_section(subsection)
        LOGGER.info("Navigate to %s -> %s", section, subsection)


