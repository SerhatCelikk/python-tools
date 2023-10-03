import undetected_chromedriver as uc

# Initialize a webdriver instance (this doesn't open a browser window)
driver = uc.Chrome()

# Get the ChromeDriver version
driver_version = driver.capabilities['chrome']['chromedriverVersion']

# Print the ChromeDriver version
print(driver_version)

# Close the webdriver
driver.quit()
