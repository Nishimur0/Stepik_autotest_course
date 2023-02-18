from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
link = 'https://parsinger.ru/selenium/7/7.html'
summary = 0
result = 0
try:
    browser.get(link)
    find_elms = browser.find_elements(By.TAG_NAME, 'option')
    for item in find_elms:
        summary += int(item.text)
    result = browser.find_element(By.ID, 'input_result')
    result.send_keys(summary) 
    submit = browser.find_element(By.ID, 'sendbutton')
    submit.click()
    pr_result = browser.find_element(By.ID, 'result')
    result = pr_result.text
    
    in_fin = result
    browser.get('https://stepik.org/lesson/731861/step/10?unit=733396')
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'ember58')))
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
    browser.get('https://stepik.org/lesson/731861/step/10?unit=733396')
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