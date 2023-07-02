from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER = "C:\Development\chromedriver"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3590309263&f_AL=true&f_WT=2&geoId=101165590&keywords=android%20developer&location=United%20Kingdom&refresh=true"
EMAIL = "**********"
PASSWORD = "**********"

service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service)

driver.get(url=URL)
driver.maximize_window()
Sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
Sign_in.click()

time.sleep(5)

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(EMAIL)
pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys(PASSWORD)
pass_input.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    job_save = driver.find_element(By.CLASS_NAME, "jobs-save-button ")
    job_save.click()
input(Keys.ENTER)
time.sleep(5)
driver.quit()
