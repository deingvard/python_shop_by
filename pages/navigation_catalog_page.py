from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class NavigationCatalogPageLocators(BasePage):
    sections = Finds(by=By.XPATH, value="//span[contains(@class, 'Catalog__SectionLevel1')]")
    subsections = Finds(by=By.XPATH, value="//span[contains(@class, 'Catalog__SectionLevel3')]/a")
    choose_laptop = Find(by=By.XPATH, value='.//*[@class="VisitSection__BlockRecipesName"]//*[text()="Ноутбуки"]')
