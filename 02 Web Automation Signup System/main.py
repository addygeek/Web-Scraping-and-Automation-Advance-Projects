import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Absolute path to ChromeDriver
chromedriver_path = r"D:\PROGRAMING\Web scapper\Python Web Scrapper Project\Chrome Driver\chromedriver.exe"

# Check if the ChromeDriver path is valid
if not os.path.isfile(chromedriver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

# Set up the ChromeDriver service
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("http://automationpractice.com")

    # Maximize the window
    driver.maximize_window()

    # Navigate to Sign in page
    driver.find_element(By.LINK_TEXT, "Sign in").click()

    # Click on 'Create an account' to register a new user
    email = "testuser@example.com"  # Replace with a unique email for each test
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email_create"))).send_keys(email)
    driver.find_element(By.ID, "SubmitCreate").click()

    # Fill out the registration form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()  # Select Mr.
    driver.find_element(By.ID, "customer_firstname").send_keys("Test")
    driver.find_element(By.ID, "customer_lastname").send_keys("User")
    driver.find_element(By.ID, "passwd").send_keys("SecurePass123")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "city").send_keys("Test City")
    driver.find_element(By.ID, "id_state").send_keys("California")
    driver.find_element(By.ID, "postcode").send_keys("90001")
    driver.find_element(By.ID, "phone_mobile").send_keys("1234567890")
    driver.find_element(By.ID, "submitAccount").click()

    # Wait for the account creation to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "account")))

    # Log out
    driver.find_element(By.CLASS_NAME, "logout").click()

    # Navigate to Sign in page again
    driver.find_element(By.LINK_TEXT, "Sign in").click()

    # Perform login with the newly created account
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    driver.find_element(By.ID, "passwd").send_keys("SecurePass123")
    driver.find_element(By.ID, "SubmitLogin").click()

    # Wait for successful login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "account")))

    # Sleep for demonstration purposes
    time.sleep(5)

finally:
    # Clean up
    driver.quit()
