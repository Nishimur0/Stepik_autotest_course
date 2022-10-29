from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

browser.get(link)
try:
    lin = browser.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x0 = browser.find_element(By.ID, 'input_value')
    x1 = x0.text
    x = int(x1)
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    sub = browser.find_element(By.CLASS_NAME, 'btn-primary')
    sub.click()  
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    time.sleep(4)
    browser.quit()