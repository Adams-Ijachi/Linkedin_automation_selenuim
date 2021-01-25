import selenium
import time
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)


driver.get("https://www.linkedin.com/")
username = driver.find_element_by_id("session_key")
username.send_keys("???") #### YOUR LINKEDIN USERNAME 
username.send_keys(Keys.RETURN)
password = driver.find_element_by_id("session_password")
password.send_keys("???") #### YOUR LINKEDIN PASSWORD
password.send_keys(Keys.RETURN)

myElem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.theme--mercado .share-box-feed-entry__trigger--v2')))
myElem.send_keys(Keys.RETURN)
time.sleep(3)
modal = driver.find_element_by_class_name("ql-editor")

post_reader = open("text.txt", "r")
post = post_reader.read()

modal.send_keys(post)
post_btn = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[3]/button')

post_btn.send_keys(Keys.RETURN)

# driver.quit() TO CLOSE THE DRIVER