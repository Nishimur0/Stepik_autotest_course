from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'
def summa(a, b):
    return a + b

try:
    browser.get(link)
    a0 = browser.find_element(By.ID, 'num1')
    b0 = browser.find_element(By.ID, 'num2')
    a1 = a0.text
    b1 = b0.text
    a = int(a1)
    b = int(b1)
    y = summa(a, b)
    y1 = str(y)
    sel = Select(browser.find_element(By.TAG_NAME, 'select'))
    sel.select_by_visible_text(y1)
    browser.find_element(By.CLASS_NAME, 'btn-default').click()
   # ищем элемент с текстом "Python"
   # Можно еще 2 метода: select.select_by_visible_text("text") и select.select_by_index(index).
finally:
    time.sleep(3)
    browser.quit()