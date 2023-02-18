from selenium import webdriver
from selenium.webdriver.common.by import By

brows = webdriver.Chrome()
link = 'https://parsinger.ru/selenium/3/3.html'
total = 0
try:
    brows.get(link)
    all_p2 = brows.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    lst = []
    for i in range(len(all_p2)):
        lst.append(int(all_p2[i].text))
    total = sum(lst)
    print(total)
finally:
    brows.quit()
