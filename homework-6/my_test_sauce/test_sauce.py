import uuid
from datetime import date
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

from my_test_sauce import constants
import pytest


class TestSauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(constants.URL)
        self.folder_path = str(date.today())
        Path(self.folder_path).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.save_screenshot(f"{self.folder_path}/{uuid.uuid4()}.png")
        self.driver.quit()

    @pytest.mark.parametrize("username,password", constants.INVALID_LOGIN_DATA)
    def test_check_if_invalid_login(self, username, password):
        self.input_wait(constants.USERNAME_INPUT_XPATH).send_keys(username)
        self.input_wait(constants.PASSWORD_INPUT_XPATH).send_keys(password)
        self.input_wait(constants.LOGIN_BUTTON_XPATH).click()
        error_message = self.input_wait(constants.ERROR_MESSAGE_XPATH)

        assert error_message.text == constants.INVALID_ERROR_MESSAGE

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login(self, username, password):
        self.input_wait(constants.USERNAME_INPUT_XPATH).send_keys(username)
        self.input_wait(constants.PASSWORD_INPUT_XPATH).send_keys(password)
        self.input_wait(constants.LOGIN_BUTTON_XPATH).click()
        current_url = self.driver.current_url

        assert current_url == constants.EXPECTED_URL

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_about_page_is_opened(self, username, password):
        TestSauce.test_check_if_success_login(self, username, password)
        self.input_wait(constants.MENU_BUTTON_XPATH).click()
        self.input_wait(constants.ABOUT_BUTTON_XPATH).click()
        current_url = self.driver.current_url

        assert current_url == constants.EXPECTED_ABOUT_URL

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_logout(self, username, password):
        TestSauce.test_check_if_success_login(self, username, password)
        self.input_wait(constants.MENU_BUTTON_XPATH).click()
        self.input_wait(constants.LOGOUT_BUTTON_XPATH).click()
        current_url = self.driver.current_url

        assert current_url == constants.URL

    @pytest.mark.parametrize("username,password", constants.VALID_LOGIN_DATA)
    def test_check_if_success_login_add_to_cart_remove_from_cart(self, username, password):
        TestSauce.test_check_if_success_login(self, username, password)
        self.input_wait(constants.ADD_TO_CART_BUTTON_XPATH).click()
        self.input_wait(constants.CART_BADGE_XPATH).click()
        self.input_wait(constants.REMOVE_BUTTON_XPATH).click()
        cart_badge = self.input_wait(constants.CART_BADGE_XPATH)

        assert cart_badge.text == constants.CART_BADGE_TEXT

    def input_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator)
