import uuid
from datetime import date
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

import constants
import pytest


class TestSauceDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(constants.URL)
        self.folder_path = str(date.today())
        Path(self.folder_path).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.save_screenshot(f"{self.folder_path}/{uuid.uuid4()}.png")
        self.driver.quit()

    def test_check_if_username_password_are_empty(self):
        self.input_text(constants.LOGIN_BUTTON_XPATH).click()
        error_message = self.input_text(constants.ERROR_MESSAGE_XPATH)

        assert error_message.text == constants.USERNAME_ERROR_MESSAGE

    @pytest.mark.parametrize("username,password", constants.INVALID_LOGIN_DATA)
    def test_check_if_password_is_empty(self, username, password):
        self.input_text(constants.USERNAME_INPUT_XPATH).send_keys(username)
        self.input_text(constants.PASSWORD_INPUT_XPATH).send_keys(password)
        self.input_text(constants.LOGIN_BUTTON_XPATH).click()
        error_message = self.input_text(constants.ERROR_MESSAGE_XPATH)

        assert error_message.text == constants.PASSWORD_ERROR_MESSAGE

    @pytest.mark.parametrize("username,password", constants.LOCKED_USER_DATA)
    def test_check_if_user_has_locked_account(self, username, password):
        self.input_text(constants.USERNAME_INPUT_XPATH).send_keys(username)
        self.input_text(constants.PASSWORD_INPUT_XPATH).send_keys(password)
        self.input_text(constants.LOGIN_BUTTON_XPATH).click()
        error_message = self.input_text(constants.ERROR_MESSAGE_XPATH)

        assert error_message.text == constants.LOCKED_USER_ERROR_MESSAGE

    def test_check_if_invalid_login_error_icon(self):
        self.input_text(constants.USERNAME_INPUT_XPATH)
        self.input_text(constants.PASSWORD_INPUT_XPATH)
        self.input_text(constants.LOGIN_BUTTON_XPATH).click()

        error_icon = self.input_text(constants.ERROR_ICON_XPATH)
        error_icon.click()
        error_input_icon_passive = self.driver.find_elements(By.XPATH, constants.ERROR_INPUT_ICON_XPATH)

        assert len(error_input_icon_passive) == 0

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login(self, username, password):
        self.input_text(constants.USERNAME_INPUT_XPATH).send_keys(username)
        self.input_text(constants.PASSWORD_INPUT_XPATH).send_keys(password)
        self.input_text(constants.LOGIN_BUTTON_XPATH).click()
        current_url = self.driver.current_url

        assert current_url == constants.EXPECTED_URL

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_inventory_list_length(self, username, password):
        TestSauceDemo.test_check_if_success_login(self, username, password)
        inventory_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        assert len(inventory_list) == constants.INVENTORY_LIST_LENGTH

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_inventory_list_names(self, username, password):
        TestSauceDemo.test_check_if_success_login(self, username, password)
        inventory_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        inventory_list_names = []
        for inventory in inventory_list:
            inventory_list_names.append(inventory.find_element(By.CLASS_NAME, "inventory_item_name").text)

        assert inventory_list_names == constants.INVENTORY_LIST_NAMES

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_inventory_list_prices(self, username, password):
        TestSauceDemo.test_check_if_success_login(self, username, password)
        inventory_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        inventory_list_prices = []
        for inventory in inventory_list:
            inventory_list_prices.append(inventory.find_element(By.CLASS_NAME, "inventory_item_price").text)

        assert inventory_list_prices == constants.INVENTORY_LIST_PRICES

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_add_to_cart(self, username, password):
        TestSauceDemo.test_check_if_success_login(self, username, password)
        self.input_text(constants.ADD_TO_CART_BUTTON_XPATH).click()
        cart_badge = self.input_text(constants.CART_BADGE_XPATH)

        assert cart_badge.text == constants.CART_BADGE_TEXT

    def input_text(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator)
