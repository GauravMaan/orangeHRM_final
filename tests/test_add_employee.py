import pytest
import time
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.PIMPage import PIMPage
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="session")
def driver():
    # Initialize Safari driver; modify as needed for other browsers.
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_employee(driver):
    base_url = "https://opensource-demo.orangehrmlive.com/"

    logger.info("Navigating to OrangeHRM login page")
    driver.get(base_url)
    time.sleep(2)

    # Verify login page
    assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

    login_page = LoginPage(driver)
    logger.info("Performing login with valid credentials")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # Wait for login to complete; consider using explicit waits for a dashboard element
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower(), "Login Failed!"
    logger.info("Login successful")

    pim_page = PIMPage(driver)
    logger.info("Navigating to PIM section")
    pim_page.navigate_to_pim()
    time.sleep(2)

    logger.info("Clicking Add Employee")
    pim_page.click_add_employee()
    time.sleep(2)

    logger.info("Adding employee details")
    pim_page.add_employee("Gaurav", "Kumar", "12345")
    time.sleep(6)

    logger.info("Searching for the added employee")
    pim_page.search_employee("Gaurav")
    time.sleep(5)

    logger.info("Test for adding employee completed successfully!")