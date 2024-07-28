import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Absolute path to ChromeDriver
chromedriver_path = r"D:\PROGRAMING\Web scapper\Python Web Scrapper Project\01 My Github Automation Open\chromedriver.exe"

# Check if the ChromeDriver path is valid
if not os.path.isfile(chromedriver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

try:
    # Initialize the ChromeDriver service
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://google.com")
    logging.info("Opened Google homepage")

    # Wait until the search box is present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys("GitHub addygeek" + Keys.ENTER)
    logging.info("Entered search term and submitted")

    # Wait until the search results are present
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "addygeek"))
    )
    link.click()
    logging.info("Clicked on the 'addygeek GitHub' link")

    # Wait for the new page to load completely by ensuring a known element is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "vcard-names"))
    )
    logging.info("New page loaded")

    # Keep the browser open for inspection
    time.sleep(300)  # Wait for 5 minutes (300 seconds)

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Uncomment this line if you want to close the browser after the inspection period
    # driver.quit()
    logging.info("Finished execution")
