from selenium.webdriver.common.by import By
import time


def open_driver(driver, url):
    driver.get(url)
    time.sleep(3)


def login(driver):
    # needed fields to sign in
    email = driver.find_element(by="id", value="session_key")
    password = driver.find_element(by="id", value="session_password")
    sign_in_button = driver.find_element(by="xpath",
                                         value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
    # set the fields
    email.send_keys("jason.nwoke@gmail.com")
    password.send_keys("birthday23")
    # sign in
    sign_in_button.click()
    time.sleep(2)


def go_to_connections(driver):
    my_network = driver.find_element(by="xpath", value='//*[@id="global-nav"]/div/nav/ul/li[2]/a')
    my_network.click()
    # wait so that the page loads
    time.sleep(3)


def process_connection(driver):
    first_section_x_path = "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section[2]/div/div[1]/div[1]"
    first_section = driver.find_element(By.XPATH, first_section_x_path)
    # get the list of accounts to connect
    accounts = first_section.find_elements(By.TAG_NAME, "li")
    # Connect with the first person in the list
    # Click the account link
    first_account_link = accounts[0].find_element(By.TAG_NAME, "a")
    first_account_link.click()
    # wait so that the page loads
    time.sleep(2)

    # get the person's name
    connection_name = driver.find_element(By.TAG_NAME, "h1").text
    first_name = connection_name.split(" ")[0]
    # get the connect button
    x_path = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button'
    connect_button = driver.find_element(By.XPATH, x_path)
    # if this button is not the connect button, return to go to the next person
    if connect_button.text != "Connect":
        return False
    connect_button.click()
    # wait so that the page loads
    time.sleep(2)

    # click the add note button
    add_note_x_path = '/html/body/div[3]/div/div/div[3]/button[1]'
    add_note_button = driver.find_element(By.XPATH, add_note_x_path)
    add_note_button.click()
    time.sleep(2)

    # add the connection message
    text_area_x_path = '/html/body/div[3]/div/div/div[2]/div/textarea'
    text_area = driver.find_element(By.XPATH, text_area_x_path)
    message = """Hey %s,

    I am expanding my network and would love to connect with you! I look forward to our future communication.

    - Obinna""" % first_name
    text_area.send_keys(message)
    time.sleep(1)

    # send the connection
    send_connection_x_path = '/html/body/div[3]/div/div/div[3]/button[2]'
    send_button = driver.find_element(By.XPATH, send_connection_x_path)
    send_button.click()
    time.sleep(2)
    print("""--------- New connection: %s ---------""" % connection_name)
    return True
