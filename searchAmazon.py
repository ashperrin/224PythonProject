# search amazon
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys

import db_connector

def search(driver, userid, database, search_in = 0):

    if search_in == 0:
        userInput = input("Enter any item you would like to search for on Amazon : ")
    else:
        userInput = search_in

    # Add the search to user's search history in the database
    if database != 0:
        if userid != 1:
            shop_db = db_connector.connect()
            query = "INSERT INTO History(UserId, RecentSearches) VALUES (\'%s', '%s')" % (userid, str(userInput))
            shop_db.commit()

    driver.get('https://www.amazon.com')
    driver.implicitly_wait(5)

    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(userInput)
    search_box.send_keys(Keys.RETURN)

    if(search_in == 0):
        print()

    # get info of first item
    name = getItemName(driver)
    price = getItemPrice(driver)

    output = ""

    if search_in  == 0:
        print("Item: " + name[0])
        print("Price: " + price[0] + "." + price[1])
        print("Item: " + name[1])
        print("Price: " + price[2] + "." + price[3])
        print("Item: " + name[2])
        print("Price: " + price[4] + "." + price[5])


    output += "Item: " + name[0] + "\n"
    output += "Price: " + price[0] + "." + price[1] + "\n\n"
    output += "Item: " + name[1] + "\n"
    output += "Price: " + price[2] + "." + price[3] + "\n\n"
    output += "Item: " + name[2] + "\n"
    output += "Price: " + price[4] + "." + price[5] + "\n\n"

    priceAsDouble = int(price[0]) + (int(price[1]) / 100)

    return output

def getItemName(driver):
    driver.implicitly_wait(10)
    item = driver.find_elements_by_xpath("//*[@class='a-link-normal a-text-normal']")
    if len(item) > 0:
        return item[0].text,item[1].text,item[2].text


    return "ITEM NOT FOUND"

def getItemPrice(driver):
    driver.implicitly_wait(10)
    priceWhole = driver.find_elements_by_class_name('a-price-whole')
    priceDec = driver.find_elements_by_class_name('a-price-fraction')

    if(len(priceWhole) > 0 and len(priceDec) > 0):
        return priceWhole[0].text, priceDec[0].text, priceWhole[1].text, priceDec[1].text, priceWhole[2].text, priceDec[2].text

    return "PRICE NOT FOUND"
