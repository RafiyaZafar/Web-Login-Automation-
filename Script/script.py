# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



# Declare driver as a global variable
driver = None

def startAutoBot(email, password, url):

    global driver  # Declare driver as global to make it accessible outside the function


    # Get the path of chromedriver which you have install
    path = "C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe"

    

    service = Service(path)
    driver = webdriver.Chrome(service=service)

    # opening the website  in chrome.
    driver.get(url)

    
    # Find the email input field by name and enter the email
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(email)

    # Find the password input field by name and enter the password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Click on the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='button']")
    login_button.click()
    

# Driver Code
# Enter below your login credentials
email = "fiyazafar@gmail.com"
password = "Bebo@1234"
 
# URL of the login page of site
# which you want to automate login.
url = "https://www.quora.com/"
 
# Call the function
startAutoBot(email, password, url)

# Add a delay to keep the browser window open for 5 seconds
# time.sleep(100)

# Close the browser window
input("Press any key to close the browser...")
driver.quit()

