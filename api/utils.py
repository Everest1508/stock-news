import time
from selenium import webdriver
# %pip install webdriver_manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


def GetCSV():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36")
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    prefs = {"profile.default_content_settings.popups": 0,"download.save_directory": "F:\\VS Code\\Django\\stock-news\\NSE\\NSE\\temp\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--enable-javascript")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(
        ChromeDriverManager().install()))

    driver.get(
        'https://www.nseindia.com/companies-listing/corporate-filings-announcements')

    time.sleep(5)

    downloadcsv = driver.find_element(By.ID, 'CFanncEquity-download')

    downloadcsv.click()

    time.sleep(2)

    driver.close()