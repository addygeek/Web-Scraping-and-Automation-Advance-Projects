# GitHub Automation with ChromeDriver

This repository contains a Python project that automates the process of searching for GitHub profiles on Google, navigating to the profile page, and scrolling through the content. It leverages Selenium WebDriver for browser automation and requires Google Chrome and ChromeDriver to run.

## Features

- **User Prompt**: Prompts the user to enter a GitHub username.
- **Search Automation**: Automates the process of searching for the GitHub username on Google.
- **Profile Navigation**: Clicks on the corresponding GitHub profile link in the search results.
- **Content Scrolling**: Scrolls down the GitHub profile page to ensure all content is visible.
- **Browser Inspection**: Keeps the browser open for manual inspection after automation.

## Prerequisites

To use this script, you will need:

- **Python 3.x**: Make sure you have Python 3 installed on your machine.
- **Google Chrome**: The script is designed to work with the Google Chrome browser.
- **ChromeDriver**: A driver that allows Selenium to control Google Chrome. Ensure the ChromeDriver version matches your installed Chrome version.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/addygeek/Web-Scraping-and-Automation-Advance-Projects.git
   cd Web-Scraping-and-Automation-Advance-Projects/01 My Github Automation/
   ```

2. **Install Dependencies**:
   Use `pip` to install the required Python packages.
   ```sh
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**:
   Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and ensure it is accessible from your PATH.

## Usage

1. **Run the Script**:
   Execute the main script by running:
   ```sh
   python main.py
   ```

2. **Follow Prompts**:
   - Enter the GitHub username when prompted.

3. **Automation in Action**:
   - The script will open Google Chrome, search for the specified GitHub username, navigate to the profile, and scroll through the page.

## Files

- `main.py`: The main Python script that contains the automation logic.
- `Readme.md`: Documentation for the project.
- `Master Python Web Scraping & Automation using BS4 & Selenium Certifcation.pdf`: A certificate for mastering web scraping and automation using BeautifulSoup and Selenium.
- `Web Automation and Scraping using Python Certification Udemy.pdf`: A certification document for web automation and scraping using Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Selenium**: For providing a robust tool for browser automation.
- **Udemy**: For courses that helped in mastering Python web scraping and automation.

## Contact

For any questions or issues, please contact [addygeek](https://github.com/addygeek).
