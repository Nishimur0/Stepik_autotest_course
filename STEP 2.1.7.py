from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    x0 = browser.find_element(By.CSS_SELECTOR, '[valuex]')
    x1 = x0.get_attribute('valuex')
    x = int(x1)
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '[id=answer]')
    answer.send_keys(y)
    cbx = browser.find_element(By.CSS_SELECTOR, '[id=robotCheckbox]')
    cbx.click()
    rob = browser.find_element(By.CSS_SELECTOR, '[id=robotsRule]')
    rob.click()
    sub = browser.find_element(By.CLASS_NAME, 'btn-default')
    sub.click()


    
finally:
    time.sleep(3)
    browser.quit()
