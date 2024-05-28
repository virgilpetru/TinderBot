from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import requests


import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#driver.maximize_window()

FB_EMAIL = "YOUR FACEBOOK ADDRESS"
FB_PW = "YOUR FACEBOOK PASSWORD"

driver.get("https://tinder.com")

#Accept cookies tinder
time.sleep(2)
accept_cookies_t = driver.find_element(By.XPATH, value='//*[@id="q-1308614829"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_cookies_t.click()

# Log in
log_in = driver.find_element(By.XPATH, '//*[@id="q-1308614829"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
log_in.click()

time.sleep(4)
pick_facebook = driver.find_element(By.XPATH, '//*[@id="q-1087274393"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
window_before = driver.window_handles[0]
pick_facebook.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

#Accept cookies facebook
time.sleep(3)
accept_cookies_f = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
accept_cookies_f.click()

#Facebook Log in
time.sleep(2)
facebook = driver.find_element(By.ID, 'email')
facebook.send_keys(FB_EMAIL)
password = driver.find_element(By.ID, 'pass')
password.send_keys(FB_PW)
login = driver.find_element(By.NAME, 'login')
login.click()

driver.switch_to.window(window_before)

#Location Accept
time.sleep(8)
location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
location.click()

#Notifications Accept
time.sleep(5)
notification = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification.click()

# See who likes you
try:
    time.sleep(4)
    see_who = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[3]/button[2]/div[2]/div[2]')
    see_who.click()
except NoSuchElementException:
    time.sleep(2)

for n in range(30):
    time.sleep(5)
    try:
        swipe_right = driver.find_element(By.XPATH, value='//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(4)