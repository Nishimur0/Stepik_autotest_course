from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = str(input())
password = str(input())

with webdriver.Chrome() as asd:
    asd.get('https://www.yclients.com/signin/')
    asd.maximize_window()
    button = WebDriverWait(asd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    logn = asd.find_element(By.CSS_SELECTOR, "[name='email']")
    logn.click()
    logn.send_keys(login)
    paswd = asd.find_element(By.CSS_SELECTOR, '[type="password"]')
    paswd.click()
    paswd.send_keys(password)
    button.click()
    time.sleep(4)
    cookies = asd.get_cookies()
    pprint(cookies)