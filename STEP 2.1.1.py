from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
  browser.get(link)
  x_element = browser.find_element(By.CSS_SELECTOR, '[id=input_value]')
  x = x_element.text
  y = calc(x)
  y_el = browser.find_element(By.CSS_SELECTOR, '[id=answer]')
  y_el.send_keys(y)
  chbx = browser.find_element(By.CSS_SELECTOR, '[id=robotCheckbox]')
  chbx.click()
  robot = browser.find_element(By.CSS_SELECTOR, '[id=robotsRule]')
  robot.click()
  sbmt = browser.find_element(By.CLASS_NAME, 'btn-default')
  sbmt.click()
  
finally:
  time.sleep(7)
  browser.quit()