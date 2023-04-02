from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
link = 'https://parsinger.ru/scroll/2/index.html'
result = 0
try:
    browser.get(link)
    chbx = browser.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')

    for i in range(len(chbx)):
        action = ActionChains(browser)
        action.move_to_element(chbx[i])
        action.click()
        action.perform()
        res = browser.find_element(By.ID, f'result{i+1}')
        if res.text == '':
            continue
        else:
            result += int(res.text)

    qwerty = result
    browser.get('https://stepik.org/lesson/732069/step/1?unit=733602')
    button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, 'ember53')))
    log = browser.find_element(By.ID, 'ember53')
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
    browser.get('https://stepik.org/lesson/732069/step/1?unit=733602')
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

