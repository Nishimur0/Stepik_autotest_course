from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
brsr = webdriver.Chrome()
lnk = 'https://parsinger.ru/selenium/3/3.html'
total = 0
try:
    sm = []
    brsr.get(lnk)
    all_in = brsr.find_elements(By.XPATH, "//div[@class='text']/p[1]")
    all_in2 = brsr.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    all_in3 = brsr.find_elements(By.XPATH, "//div[@class='text']/p[3]")
    for i in range(len(all_in)):
        sm.append(int(all_in[i].text))
        
    for k in range(len(all_in2)):
        sm.append(int(all_in2[k].text))
        
    for x in range(len(all_in3)):
        sm.append(int(all_in3[x].text))

    total = sum(sm)
    print(total)

finally:
    brsr.quit()