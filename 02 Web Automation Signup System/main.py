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
chromedriver_path = r"D:\PROGRAMING\Web scapper\Python Web Scrapper Project\Chrome Driver\chromedriver.exe"

# Check if the ChromeDriver path is valid
if not os.path.isfile(chromedriver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")
