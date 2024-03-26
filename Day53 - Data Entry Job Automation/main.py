from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time


# Scrape with Beautiful Soup:
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

# Get a list of all listings URLs
listings = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
listing_urls = [listing.get('href') for listing in listings]
print(listing_urls)

# Get a list of all listings prices
listings = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
listing_prices = [listing.getText()[0:6] for listing in listings]
print(listing_prices)

# Get a list of all listings addresses
listings = soup.find_all(name="address")
listing_addresses = [listing.getText().strip() for listing in listings]
listing_addresses = [listing.replace("|", "").replace("+", "") for listing in listing_addresses]
print(listing_addresses)

# Selenium Google Form

# Keep browser open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc-p5JCLWZ9cNcOPz2eH4QnmfdRKafOJhEK_TR3BVvvdYx-fQ/viewform?usp=sf_link")
time.sleep(2)

# Loop through the data and do data entry
for i in range(len(listing_urls)):

    # Find all input text fields
    input_text_fields = driver.find_elements(By.XPATH, '//input[@type="text"]')

    # Fill in address
    input_text_fields[0].send_keys(listing_addresses[i])

    # Fill in price
    input_text_fields[1].send_keys(listing_prices[i])

    # Fill in URL
    input_text_fields[2].send_keys(listing_urls[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(1)

    # Submit another response
    submit_again = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_again.click()
    time.sleep(1)

# Close browser
driver.quit()
