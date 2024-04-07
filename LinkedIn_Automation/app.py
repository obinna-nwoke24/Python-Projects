from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from functions import open_driver, login, go_to_connections, process_connection

################ Step 1: Setup the web driver ################
# Load the Chrome web driver
driver = webdriver.Chrome()
# use the LinkedIn home page to log in
linkedin = "https://linkedin.com/home"
# use the driver to go to the LinkedIn home page
open_driver(driver, linkedin)

################ Step 2: Log-in ################
login(driver)

################ Step 3: User prompt if security question pops up (optional) ################
user_response = None
while user_response not in ["y", "Y"]:
    user_response = input("""Ready to run connections bot [y or Y]:""")

################ Step 4: Loop to add N connections ################
num_connections = 0
while num_connections < 10:
    try:
        go_to_connections(driver)
        new_connection = process_connection(driver)
        if new_connection:
            num_connections += 1
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException:
        pass

# close the driver
driver.quit()
print("LinkedIn bot complete")
