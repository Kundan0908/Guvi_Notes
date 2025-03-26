import json
import time
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from PageObjects.checkout import Checkout
from PageObjects.Homepage import Homepage
from PageObjects.login import Testlogin

test_data_path = r'C:\Users\Kundan_Kumar\PycharmProjects\Demo_Guvi\Oops_python\data\test_e2e_Data.json'

with open(test_data_path, mode='r') as f:
    test_data = json.load(f)
    test_data = test_data['data']

@pytest.mark.parametrize("testdata",test_data)
def test_E2E_chrome(InvokeBrowser,testdata):
    driver = InvokeBrowser
    driver.maximize_window()
    login = Testlogin(driver)
    sleep(2)
    login.login_(testdata["Username"],testdata["Password"])
    homepage = Homepage(driver)
    sleep(3)
    homepage.add_product_to_cart(testdata["product_type"])
    sleep(3)
    checkout_ = Checkout(driver)
    checkout_.place_order()
    sleep(3)
    checkout_.checkout_details(testdata["order_name"],testdata["order_country"],testdata["order_city"],testdata["order_card"],
                               testdata["order_month"],testdata["order_year"])
    checkout_.confirm_order()
    checkout_.verify_order()