import time
######################################
# Test "Shop.by" #
######################################

def test_search(app, config):
    app.open_home_page()
    app.navigation_catalog.navigate_to("Компьютеры", "Ноутбуки")
    app.laptops.choose_laptop_name("Lenovo")
    # app.laptops.choose_laptop_name("Dell")
    # app.laptops.choose_laptop_name("HP")
    # app.laptops.choose_laptop_price("700", "1500")
    # app.laptops.click_show_diagonal()
    # app.laptops.choose_laptops_diagonal("15")
    # app.laptops.choose_laptops_diagonal("17")

    time.sleep(5)

