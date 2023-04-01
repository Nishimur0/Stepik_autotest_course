from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

browser.get(link)
first = browser.find_element(By.CSS_SELECTOR, '[name=firstname]')
first.send_keys('Ivan')
second = browser.find_element(By.CSS_SELECTOR, '[name=lastname]')
second.send_keys('Bolvan')
email = browser.find_element(By.CSS_SELECTOR, '[name=email]')
email.send_keys('ivan@bolvan.po')
file = browser.find_element(By.ID, 'file')
file.send_keys('C:/Users/darka/Desktop/file.txt')
btn = browser.find_element(By.CLASS_NAME, 'btn-primary').click()
