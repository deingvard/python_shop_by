from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find
import logging

from webium.controls.select import Select

LOGGER = logging.getLogger(__name__)


class LaptopsPageLocators(BasePage):
    laptops_name = Finds(by=By.XPATH, value='.//*[@class="ModelFilter__CheckboxLink"]/a')

    laptops_price_min_input = Find(by=By.CSS_SELECTOR, value="#minnum_45")
    laptops_price_max_input = Find(by=By.CSS_SELECTOR, value="#maxnum_45")

    show_laptops_diagonal_results = Find(by=By.XPATH, value=".//*[@id='Attr_prof_5828']/div/div[2]/span[1]")

    diagonal_checkbox = Finds(by=By.XPATH, value='.//*[@class="ModelFilter__CheckboxLink"]')
