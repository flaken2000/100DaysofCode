from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL", "Env variable LINKEDIN_EMAIL doesn't exists")
LINKEDIN_PASS = os.environ.get("LINKEDIN_PASS", "Env variable LINKEDIN_PASS doesn't exists")
JOB_SEARCH = "cloud infrastructure developer"

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(2)

# Log in
email = driver.find_element(By.ID, value="username")
email.send_keys(LINKEDIN_EMAIL)

passw = driver.find_element(By.ID, value="password")
passw.send_keys(LINKEDIN_PASS)

# Click on log in button
log_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
log_in.click()
time.sleep(4)

# Search for a role
role = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
role.send_keys(JOB_SEARCH, Keys.ENTER)
time.sleep(3)

# Filter on Jobs
filter_job = driver.find_element(By.CSS_SELECTOR, ".search-reusables__primary-filter button")
filter_job.click()
time.sleep(4)

# Get all the jobs
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

# For each job, click on the job and sleep for 2 seconds.
# Not doing anything else for now. If I wanted to save the job,
# I could just do:
#save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
#save.click()

for job in all_jobs:
    print(job.text)
    job.click()
    time.sleep(1)

# Close browser
#driver.quit()
