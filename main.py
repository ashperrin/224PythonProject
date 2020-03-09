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

def main():
    # Welcome
    print("\tWelcome to your Amazon personal shopper bot!\n\t\t\tHappy shopping")
    print()

    driver = parseArguements()

    # Login
    print("You are not logged in")
    log = input("Login? (y/n): ")
    if log.lower() == 'y':
        login(driver)

    # Search
    search(driver)

    # Time to live
    time.sleep(5)
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
