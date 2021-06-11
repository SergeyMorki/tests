import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)
#pools = .pools.curr1.ng-star-inserted
DFX_BUSD = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(1)').click()

DFX_BUSD = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(1)').click()


driver.quit()




