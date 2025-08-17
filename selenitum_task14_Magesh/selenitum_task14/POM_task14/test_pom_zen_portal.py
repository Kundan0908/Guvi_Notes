import time

import pytest
from loginpage import LoginPage

BASE_URL = "https://www.zenclass.in/login"
VALID_USER = "vnmmagesh@gmail.com"
VALID_PASS = "Siddhu@oct10"
INVALID_USER = "cnmmagesh@gmail.com"
INVALID_PASS = "Siddhu@dec10"

def test_login_success(driver):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.login(VALID_USER,VALID_PASS)
    assert loginpage.is_logout_displayed() == True, "Login Failed"
    loginpage.logout()
    assert "https://www.zenclass.in/" in driver.current_url

def test_login_unsuccess(driver):
    driver.get(BASE_URL)
    loginpage=LoginPage(driver)
    loginpage.login(INVALID_USER,INVALID_PASS)
    assert "https://www.zenclass.in/login" in driver.current_url.lower()

def test_username_input(driver):
    driver.get(BASE_URL)
    username_input = driver.find_element(*LoginPage.username_locator)
    username_input.send_keys("vnmmagesh@gmail.com")
    assert username_input.get_attribute("value") == "vnmmagesh@gmail.com"

def test_password_input(driver):
    driver.get(BASE_URL)
    password_input = driver.find_element(LoginPage.self.password_locator)
    password_input.send_keys("Siddhu@oct10")
    assert password_input.get_attribute("value") == "Siddhu@oct10"

def test_submit_button(driver):
    driver.get(BASE_URL)
    submit_btn = driver.find_element(*LoginPage.login_button_locator)
    assert submit_btn.is_enabled()
