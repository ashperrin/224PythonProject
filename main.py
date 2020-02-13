import time
from selenium import webdriver # main webdriver
from selenium.webdriver.common.keys import Keys # for sending keys
from selenium.webdriver.chrome.options import Options # for adding headless option

def main():


    options = Options()
    options.headless = False # make true if you do not want to not want to see the browser
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.amazon.com')

    input = "fallout 4 game of the year"
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(input)
    search_box.send_keys(Keys.RETURN)

    time.sleep(10) # time to live
    driver.close()

if __name__ == '__main__':
    main()
