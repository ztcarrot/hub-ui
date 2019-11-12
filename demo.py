# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.homePage import homePage as hubHome
browser = webdriver.Chrome("./drivers/chromedriver")
home = hubHome(browser)
home.open()
home.close()
#browser.get("https://www.baidu.com/")
'''
try:
    # 传入 browser 对象，总共等待20秒，每0.5秒检查一次，直到找到id为 “kw” 元素
    WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
    browser.find_element_by_id("kw").send_keys("Jay Chou")
   
except Exception:
    print('An exception flew by!')
    raise
'''


