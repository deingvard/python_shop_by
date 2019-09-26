import time
from model.group import Group


######################################
# Test "Shop.by" #
######################################

def test_search(app, config):
    app.open_home_page()
    app.navigation_catalog.navigate_to(Group(
        menu=app.config['catalog']['menu']))

    app.laptops.click_show_name_laptops()
    app.laptops.choose_laptop_name(
        app.config["laptop_manufacture"]["Lenovo"])
    app.laptops.choose_laptop_name(
        app.config["laptop_manufacture"]["Dell"])
    app.laptops.choose_laptop_name(
        app.config["laptop_manufacture"]["HP"])

    app.laptops.choose_laptop_price(Group(
        price_from=app.config['laptop_price']['price_from'],
        price_to=app.config['laptop_price']['price_to']))

    app.laptops.click_show_diagonal()
    app.laptops.choose_laptops_diagonal(
        app.config['laptop_diagonal']['diagonal_from'])
    app.laptops.choose_laptops_diagonal(
        app.config['laptop_diagonal']['diagonal_to'])

    time.sleep(4)
