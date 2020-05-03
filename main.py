#!/usr/bin/python3

# standard
import time
import sys

# external
from selenium import webdriver # main webdriver
from selenium.webdriver.chrome.options import Options # for chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions # for firefox

# self
from searchAmazon import search
from userlogin import login

def main(nonterm, search_term):

    # Welcome

    driver = parseArguements(nonterm)

    # Login
    if nonterm == 0:
        print("You are not logged in")
        log = input("Login? (y/n): ")
        if log.lower() == 'y':
            login(driver)

    # Search
    output = search(driver, search_term)

    # Time to live
    #time.sleep(5)
    driver.close()
    return output

def parseArguements(nonterm = 0):
    options = Options()

    # run with chrome GUI (default)
    if len(sys.argv) == 1 and nonterm == 0:
        options.headless = False
        driver = webdriver.Chrome(chrome_options=options)

    #run headless chrome
    if nonterm == 1 or  len(sys.argv) == 2 and sys.argv[1] == "-h":
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
    main(0, 0)
