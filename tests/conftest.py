import time
import pytest
from credential import CREDENTIAL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def chrome_driver():
    """Initialize the WebDriver once per session."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--mute-audio")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver  # Provide driver instance to tests

    driver.quit()  # Close browser after tests

@pytest.fixture(scope="class")
def driver(request, chrome_driver):
    """Login fixture that checks the class attribute for the site name."""
    site = getattr(request.cls, "site", None)  # Get site name from test class
    if not site:
        pytest.fail("Test class must define 'site' attribute")
    
    credentials = CREDENTIAL[site]
    chrome_driver.get(credentials["login_url"])  # Open login page
    chrome_driver.find_element(By.ID, "login").send_keys(credentials["username"])
    chrome_driver.find_element(By.ID, "password").send_keys(credentials["password"])
    chrome_driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[3]/button").click()

    yield chrome_driver # Provide logged-in driver to tests
    
    time.sleep(5)  