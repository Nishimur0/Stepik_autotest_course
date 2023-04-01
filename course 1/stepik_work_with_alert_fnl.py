from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
link2 = 'https://stepik.org/lesson/184253/step/4?unit=158843'
brows = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

brows.get(link)
try:
    link1 = brows.find_element(By.CLASS_NAME, 'btn-primary').click()
    alert = brows.switch_to.alert
    alert.accept()
    x0 = brows.find_element(By.ID, 'input_value')
    x = x0.text
    y = calc(x)
    answer = brows.find_element(By.ID, 'answer').send_keys(y)
    btn = brows.find_element(By.CLASS_NAME, 'btn-primary').click()
    alert2 = brows.switch_to.alert
    text = alert2.text
    print(text)


finally:
    time.sleep(3)
    brows.quit()
