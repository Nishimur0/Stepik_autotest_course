from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    x0 = browser.find_element(By.ID, 'input_value')
    x = int(x0.text)
    y = calc(x)
    inp = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
    inp.send_keys(y)
    cbx = browser.find_element(By.CSS_SELECTOR, '[id=robotCheckbox]')
    cbx.click()
    rob = browser.find_element(By.CSS_SELECTOR, '[id=robotsRule]')
    rob.click()
    sub = browser.find_element(By.CLASS_NAME, 'btn-primary')
    sub.click()
finally:
    time.sleep(4)
    browser.quit()
    