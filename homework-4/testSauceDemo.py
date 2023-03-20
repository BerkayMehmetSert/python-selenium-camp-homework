from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import constants


class TestSauceDemo:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(constants.URL)
    driver.implicitly_wait(5)

    def check_if_username_password_are_empty(self):
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, constants.ERROR_MESSAGE_XPATH)
        test_result = error_message.text == constants.USERNAME_ERROR_MESSAGE
        print(f"Username and password are empty test result is: {test_result}")

    def check_if_password_is_empty(self):
        self.driver.find_element(By.ID, "user-name").send_keys("1")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, constants.ERROR_MESSAGE_XPATH)
        test_result = error_message.text == constants.PASSWORD_ERROR_MESSAGE
        print(f"Password is empty test result is: {test_result}")

    def check_if_user_has_locked_account(self):
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, constants.ERROR_MESSAGE_XPATH)
        test_result = error_message.text == constants.LOCKED_USER_ERROR_MESSAGE
        print(f"Locked user test result is: {test_result}")

    def check_if_invalid_login_error_icon(self):
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        error_input_icon = self.driver.find_elements(By.XPATH, constants.ERROR_INPUT_ICON_XPATH)
        test_result = len(error_input_icon) == 0
        print(f"Error icon is not displayed test result is: {test_result}")
        error_icon = self.driver.find_element(By.XPATH, constants.ERROR_ICON_XPATH)
        error_icon.click()
        error_input_icon_passive = self.driver.find_elements(By.XPATH, constants.ERROR_INPUT_ICON_XPATH)
        test_result = len(error_input_icon_passive) == 0
        print(f"Error icon is not displayed test result is: {test_result}")

    def check_if_success_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        test_result = current_url == constants.EXPECTED_URL
        print(f"Success login test result is: {test_result}")

    def check_if_success_login_inventory_list_length(self):
        TestSauceDemo.check_if_success_login(self)
        inventory_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        test_result = len(inventory_list) == constants.INVENTORY_LIST_LENGTH
        print(f"Inventory list length test result is: {test_result}")


test = TestSauceDemo()
# test.check_if_username_password_are_empty()
# test.check_if_password_is_empty()
# test.check_if_user_has_locked_account()
# test.check_if_invalid_login_error_icon()
# test.check_if_success_login()
test.check_if_success_login_inventory_list_length()
