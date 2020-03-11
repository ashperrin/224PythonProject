# search amazon
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys

from db_connector import shop_db

def search(driver):
    userInput = input("Enter any item you would like to search for on Amazon : ")

    # Add the search to user's search history in the database
    # NOTE: Adjust UserId to the logged-in user's once login is implemented
    query = "INSERT INTO History(UserId, RecentSearches) VALUES (\'%s', '%s')" % (str(1), str(userInput))
    #cursor = shop_db.cursor()
    #cursor.execute(query);
    # Commit new entry into the database

    #shop_db.commit()
    driver.get('https://www.amazon.com')
    driver.implicitly_wait(5)

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
