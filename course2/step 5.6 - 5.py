from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

browser = webdriver.Chrome()
link = 'https://parsinger.ru/scroll/4/index.html'
qwerty = 0
start = 0
qwer = set()
browser.get(link)
btns = browser.find_elements(By.CLASS_NAME, 'btn')
while start != len(btns):
    try:
        for i in range(start, len(btns)):
            browser.execute_script("return arguments[0].scrollIntoView(true);", btns[i])
            btns[i].click()
            res = browser.find_element(By.ID, 'result')
            qwerty += int(res.text)
            start = i

    except ElementClickInterceptedException as blc:
        start = i

    finally:
        browser.get('https://stepik.org/lesson/732063/step/6?unit=733596')
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
        browser.get('https://stepik.org/lesson/732063/step/6?unit=733596')
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
        browser.quit()

