from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class LaptopsPageLocators(BasePage):
    parameter_laptop = Find(by=By.XPATH, value=".//*[@class='ModelFilter__CheckboxLink']//*[text()='Lenovo']")


