import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define the Selenium Grid Hub URL
SELENIUM_GRID_URL = "http://localhost:4444/wd/hub"

# Define a list of browsers to run the test on
@pytest.mark.parametrize("browser", ["chrome", "safari"])
def test_google_search(browser):
    # Define desired capabilities for the browser
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Enable headless mode
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--window-size=1920,1080")  # Set window size for headless mode
    elif browser == "safari":
        options = webdriver.SafariOptions()
        options.add_argument("--headless")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Connect to Selenium Grid
    driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)

    try:
        # Open Google
        driver.get("https://www.google.com")
        time.sleep(2)

        # Find the search bar and enter a query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Grid with PyTest")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Verify search results are displayed
        assert "Selenium" in driver.title

    finally:
        driver.quit()