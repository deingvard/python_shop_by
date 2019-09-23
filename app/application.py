from selenium import webdriver
from actions.navigation_catalogue import NavigationCatalogActions
from actions.laptops import LaptopsActions
import os
from selenium.common.exceptions import WebDriverException
import webium.settings
import logging

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self, browser, base_url):
        # Set browser
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=chrome_options,
                                           executable_path=os.getcwd() + os.sep + os.sep + "data/chromedriver")
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Sets a sticky timeout to implicitly wait for an element to be found
        self.driver.implicitly_wait(30)
        webium.settings.wait_timeout = 15
        # Invokes the window manager-specific 'full screen' operation
        self.driver.set_window_size(1980, 1020)
        # Delete all cookies in the scope of the session
        self.driver.delete_all_cookies()
        # Initialize pages
        LOGGER.info("Started browser")
        self.base_url = base_url
        self.navigation_catalog = NavigationCatalogActions(self)
        self.laptops = LaptopsActions(self)

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        LOGGER.info("Open url '%s'", self.base_url)

    def destroy(self):
        # Stop the browser
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            LOGGER.info("Browser is valid")
            return True
        except WebDriverException:
            return False

    def current_url(self):
        return self.driver.current_url
