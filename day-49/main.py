import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "jovensondon@yahoo.com"
PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(service=Service(), options=options)
driver.get(url="https://www.linkedin.com/jobs/search/"
               "?currentJobId=3707286284&f_AL=true&keywords=Python%20Developer&location=")

# Click Sign In
time.sleep(3)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Enter credentials
username = driver.find_element(By.NAME, "session_key")
username.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha: ")


