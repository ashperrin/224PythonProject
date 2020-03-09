import getpass

from db_connector import shop_db
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys

def login(driver):

    username, password = prompts()

    driver.get('https://www.amazon.com')
    driver.implicitly_wait(10)

    signin = driver.find_element_by_id("nav-link-accountList")
    signin.click()

    driver.implicitly_wait(3)
    email_box = driver.find_element_by_id("ap_email")
    email_box.send_keys(username)
    email_box.send_keys(Keys.RETURN)

    # Incorrect username
    driver.implicitly_wait(3)
    item = driver.find_elements_by_class("a-alert-heading")

    if len(item) >= 1:
        print("Error: Incorrect Password or Email, try again")
        login() # Try again

    passwd_box = driver.find_element_by_id("ap_password")
    passwd_box.send_keys(password)
    passwd_box.send_keys(Keys.RETURN)


    # Incorrect Password
    driver.implicitly_wait(3)
    item = driver.find_elements_by_class("a-alert-heading")

    if len(item) >= 1:
        print("Error: Incorrect Password or Email, try again")
        login() # Try again

    # Requires 2FA
    driver.implicitly_wait(3)
    item = driver.find_elements_by_xpath("//*[@class='a-row a-spacing-small']")

    if len(item) >= 1 and item[0].text.lower() == "authentication required":
        print("Error, 2FA is not supported. Please disable or continue without login")
        return 1


    # TODO connect to database

    #query = "INSERT INTO User(UserId, Email, Password, HistoryId) VALUES (userid, username, password, 0)"
    #cursor = shop_db.cursor()
    #cursor.execute(query)

    #Commit new entry into the database
    #shop_db.commit()
    #driver.get('https://www.amazon.com')


def getId(username):
  values = [ord(c) for c in username]
  total = sum(values)

  return total;

def prompts():
    username= input("Amazon Username/Email: ")
    userid = getId(username)
    password =getpass.getpass(prompt='Amazon Password: ', stream=None)

    return username, password
