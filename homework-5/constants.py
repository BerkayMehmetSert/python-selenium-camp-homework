URL = "https://www.saucedemo.com/"
EXPECTED_URL = "https://www.saucedemo.com/inventory.html"
USERNAME_INPUT_XPATH = "//*[@id='user-name']"
PASSWORD_INPUT_XPATH = "//*[@id='password']"
LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
ERROR_MESSAGE_XPATH = "//*[@id='login_button_container']/div/form/div[3]/h3"
ERROR_ICON_XPATH = "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button"
ERROR_INPUT_ICON_XPATH = "//div/*[@data-icon='times-circle']"
ADD_TO_CART_BUTTON_XPATH = "//*[@id='add-to-cart-sauce-labs-backpack']"
CART_BADGE_XPATH = "//*[@id='shopping_cart_container']/a/span"

USERNAME_ERROR_MESSAGE = "Epic sadface: Username is required"
PASSWORD_ERROR_MESSAGE = "Epic sadface: Password is required"
LOCKED_USER_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
INVENTORY_LIST_LENGTH = 6
INVENTORY_LIST_NAMES = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                        "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
INVENTORY_LIST_PRICES = ["$29.99", "$9.99", "$15.99", "$49.99", "$7.99", "$15.99"]
CART_BADGE_TEXT = "1"

INVALID_LOGIN_DATA = [("1", ""), ("2", ""), ("3", "")]
LOCKED_USER_DATA = [("locked_out_user", "secret_sauce")]
VALID_LOGIN_DATA = [("standard_user", "secret_sauce")]
