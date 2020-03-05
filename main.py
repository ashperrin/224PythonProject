#!/usr/bin/python3

import time
import sys

from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys
from selenium.webdriver.chrome.options import Options # for chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions # for firefox

from db_connector import shop_db

def main():

    print("    Welcome to your Amazon personal shopper bot!\n                Happy shopping")

    userInput = input("Enter any item you would like to search for on Amazon : ")
    driver = parseArguements()

    # Add the search to user's search history in the database
    # NOTE: Adjust UserId to the logged-in user's once login is implemented
    
    query = "INSERT INTO History(UserId, RecentSearches) VALUES (1, " + "'" + str(userInput) + "'" + ")"
    cursor = shop_db.cursor()
    cursor.execute(query)

    # Commit new entry into the database
    shop_db.commit()

    driver.get('https://www.amazon.com')

    # search amazon
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(userInput)
    search_box.send_keys(Keys.RETURN)
    print()

    # get info of first item
    name = getItemName(userInput, driver)
    price = getItemPrice(driver)
    print("Item: " + name)
    if price != "PRICE NOT FOUND":
        print("Price: " + price[0] + "." + price[1])
        priceAsDouble = int(price[0]) + (int(price[1]) / 100)

    time.sleep(10) # time to live
    driver.close()

def userLogin():
    # TODO:
    return 0

# TODO get better filtering
def getItemName(name, driver):
    driver.implicitly_wait(10)
    item = driver.find_elements_by_xpath("//*[@class='a-link-normal a-text-normal']")
    if len(item) > 0:
        return item[0].text

    return "ITEM NOT FOUND"

def getItemPrice(driver):
    driver.implicitly_wait(10)
    priceWhole = driver.find_elements_by_class_name('a-price-whole')
    priceDec = driver.find_elements_by_class_name('a-price-fraction')

    if(len(priceWhole) > 0 and len(priceDec) > 0):
        return priceWhole[0].text, priceDec[0].text

    return "PRICE NOT FOUND"

def parseArguements():
    options = Options()

    # run with chrome GUI (default)
    if len(sys.argv) == 1:
        options.headless = False
        driver = webdriver.Chrome(chrome_options=options)

    #run headless chrome
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)

    #run with firefox 32bit
    if len(sys.argv) == 2 and sys.argv[1] == "-f":
        driver=webdriver.Firefox()

    #run with firefox 32bit headless
    if len(sys.argv) ==3 and sys.argv[2] == "-h":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    return driver


if __name__ == '__main__':
    main()
