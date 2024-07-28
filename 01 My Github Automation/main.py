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
chromedriver_path = r"D:\PROGRAMING\Web scapper\Python Web Scrapper Project\01 My Github Automation\chromedriver.exe"

# Check if the ChromeDriver path is valid
if not os.path.isfile(chromedriver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

# Prompt user for GitHub username
github_username = input("Enter the GitHub username to search for: ")

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
    search_box.send_keys(f"GitHub {github_username}" + Keys.ENTER)
    logging.info(f"Entered search term 'GitHub {github_username}' and submitted")

    # Wait until the search results are present and click on the GitHub link
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, github_username))
    )
    link.click()
    logging.info(f"Clicked on the '{github_username}' GitHub link")

    # Wait for the new page to load completely
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "vcard-names"))
    )
    logging.info("New page loaded")

    # Scroll down the page
    # Adjust the scrolling distance as needed
    for _ in range(5):  # Scroll down 5 times
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)  # Wait for 2 seconds between scrolls

    # Keep the browser open for inspection
    time.sleep(300)  # Wait for 5 minutes (300 seconds)

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Uncomment this line if you want to close the browser after the inspection period
    # driver.quit()
    logging.info("Finished execution")
