#!/usr/bin/python3

import time
import sys
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys
from selenium.webdriver.chrome.options import Options # for chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions # for firefox

def main():
    driver = parseArguements()

    driver.get('https://www.amazon.com')

    input = "fallout 4 game of the year"
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(input)
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
