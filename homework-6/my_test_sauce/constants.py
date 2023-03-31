URL = "https://www.saucedemo.com/"
EXPECTED_URL = "https://www.saucedemo.com/inventory.html"
EXPECTED_ABOUT_URL = "https://saucelabs.com/"
USERNAME_INPUT_XPATH = "//*[@id='user-name']"
PASSWORD_INPUT_XPATH = "//*[@id='password']"
LOGIN_BUTTON_XPATH = "//*[@id='login-button']"
ERROR_MESSAGE_XPATH = "//*[@id='login_button_container']/div/form/div[3]/h3"
ADD_TO_CART_BUTTON_XPATH = "//*[@id='add-to-cart-sauce-labs-backpack']"
REMOVE_BUTTON_XPATH = "//*[@id='remove-sauce-labs-backpack']"
CART_BADGE_XPATH = "//*[@id='shopping_cart_container']/a"
MENU_BUTTON_XPATH = "//*[@id='react-burger-menu-btn']"
ABOUT_BUTTON_XPATH = "//*[@id='about_sidebar_link']"
LOGOUT_BUTTON_XPATH = "//*[@id='logout_sidebar_link']"

INVALID_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
LOCKED_USER_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
CART_BADGE_TEXT = ""

INVALID_LOGIN_DATA = [("invalid_user", "invalid_password"), ("standard_user", "invalid_password")]
VALID_LOGIN_DATA = [("standard_user", "secret_sauce")]
