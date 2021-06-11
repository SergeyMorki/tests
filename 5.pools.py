import time
from selenium import webdriver  # импортируем webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)

pool = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(2)').click()

pool1 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(3)').click()

pool2 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(4)').click()

pool3 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(5)').click()

driver.quit()