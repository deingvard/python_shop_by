from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class LaptopsPageLocators(BasePage):
    laptops_name = Finds(by=By.XPATH, value='.//*[@class="ModelFilter__CheckboxLink"]/a')

    laptops_price_min_input = Find(by=By.XPATH, value=".//*[@id='minnum_45']")
    laptops_price_max_input = Find(by=By.XPATH, value=".//*[@id='maxnum_45']")

    laptops_diagonal_min_checkbox = Find(by=By.XPATH, value=".//*[@id='minnum_45']")
    laptops_diagonal_max_checkbox = Find(by=By.XPATH, value=".//*[@id='minnum_45']")

    show_laptops_diagonal_results = Find(by=By.XPATH, value="(//div[contains(@class, 'ModelFilter__OpenHideAttr')]//span)[5]")

