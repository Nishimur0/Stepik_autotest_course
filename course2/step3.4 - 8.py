from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
link = 'https://parsinger.ru/selenium/4/4.html'



try:
    browser.get(link)
    checks = browser.find_elements(By.CSS_SELECTOR, '[class="check"]')
    for i in checks:
        i.click()
    btn = browser.find_element(By.CSS_SELECTOR, '[class="btn"]')
    btn.click()
    result = browser.find_element(By.ID, 'result')
    in_fin = result.text
    browser.get('https://stepik.org/lesson/731861/step/8?unit=733396')
    button = WebDriverWait(browser, 5).until (EC.element_to_be_clickable((By.ID, 'ember58')))
    log = browser.find_element(By.ID, 'ember58')
    log.click()
    ent_login = browser.find_element(By.ID, 'id_login_email')
    ent_login.click()
    ent_login.send_keys('v.rychkov@yclients.tech')
    ent_pass = browser.find_element(By.ID, 'id_login_password')
    ent_pass.click()
    ent_pass.send_keys('Mandazavr1431')
    entire = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    entire.click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/731861/step/8?unit=733396')
    time.sleep(6)
    inpt0 = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="number-quiz__input number-input"]')))
    inpt = browser.find_element(
        By.CSS_SELECTOR, '[class="number-quiz__input number-input"]')
    inpt.click()
    inpt.send_keys(in_fin)
    submit = browser.find_element(
        By.CSS_SELECTOR, '[class="submit-submission"]')
    submit.click()
    time.sleep(5)
    print(in_fin)
finally:
    browser.quit()