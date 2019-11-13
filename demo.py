# encoding=utf-8
from selenium import webdriver
from util import logger
from pages.homePage import homePage as hubHome
home = hubHome("./drivers/chromedriver")
home.open()
home.searchInSearchBar("people")
#
home.browser.find_element_by_link_text("People Central")

logger.info("search people and find people central")
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


