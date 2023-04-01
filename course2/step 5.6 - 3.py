from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
link = 'https://parsinger.ru/methods/3/index.html'
qwerty = 0
try:
    browser.get(link)
    cookie = browser.get_cookies()
    for cookie in cookie:
        if int(str(cookie['name']).lstrip('secret_cookie_')) % 2 == 0 or int(str(cookie['name']).lstrip('secret_cookie_')) == 10:
            qwerty += int(cookie['value'])

    browser.get('https://stepik.org/lesson/732063/step/3?unit=733596')
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'ember55')))
    log = browser.find_element(By.ID, 'ember55')
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
    browser.get('https://stepik.org/lesson/732063/step/3?unit=733596')
    time.sleep(6)
    inpt0 = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="number-quiz__input number-input"]')))
    inpt = browser.find_element(
        By.CSS_SELECTOR, '[class="number-quiz__input number-input"]')
    inpt.click()
    inpt.send_keys(qwerty)
    submit = browser.find_element(
        By.CSS_SELECTOR, '[class="submit-submission"]')
    submit.click()
    time.sleep(5)
finally:
    browser.quit()