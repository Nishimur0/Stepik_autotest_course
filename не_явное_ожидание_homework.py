from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

txt = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
browser.find_element(By.ID, "book").click()
x0 = browser.find_element(By.ID, "input_value")
x = int(x0.text)
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "solve").click()


assert "successful" in message.text