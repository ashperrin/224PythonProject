#!/usr/bin/python3

import time
import sys
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys
from selenium.webdriver.chrome.options import Options # for chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions # for firefox

def main():
<<<<<<< HEAD
    print("    Welcome to your Amazon personal shopper bot!\n                Happy shopping")
    options = Options()
    options.headless = False # make true if you do not want to not want to see the browser
    driver = webdriver.Chrome(chrome_options=options)
=======
    driver = parseArguements()

>>>>>>> 20e4d56ef3bedfdb8e62b2168d8b1d8bbc185a7b
    driver.get('https://www.amazon.com')

    # userInput = "fallout 4 game of the year"
    userInput = input("Enter any item you would like to search for on Amazon : ")

    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(userInput)
    search_box.send_keys(Keys.RETURN)

    time.sleep(10) # time to live
    driver.close()

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
