
######################################
# Test page "Secure Area" #
######################################

def test_search(app, config):
    app.open_home_page()
    app.navigation_catalog.navigate_to("Компьютеры", "Ноутбуки")

