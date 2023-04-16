from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
link = 'https://parsinger.ru/infiniti_scroll_1/'

try:
    browser.get(link)
    browser.find_elements()
    action = ActionChains(browser)

