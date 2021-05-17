import time

from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

logo = driver.find_element_by_css_selector('.col-xl-2.col-lg-2.col-md-2.col-sm-6.col-6.logo_box').click()
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted')
users_balance.click()
Users_balances_on_Ethereum = driver.find_element_by_link_text('Users balances on Ethereum').click()
DAI_funds_holders = driver.find_element_by_link_text('DAI funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01"
driver.close()
driver.switch_to.window(current_window)

users_balance.click()
Users_balances_on_BSC = driver.find_element_by_link_text('Users balances on BSC').click()

driver.close()
driver.quit()


