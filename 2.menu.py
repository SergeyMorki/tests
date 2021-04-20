import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

medium = WebDriverWait(driver, 20).until(		# говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
        EC.element_to_be_clickable((By.LINK_TEXT, "Pools")))

DFX_BUSD = driver.find_element_by_css_selector('.header>.lp').click()

wiki = driver.find_element_by_link_text('Wiki').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://wiki.defirex.org/"
driver.close()
driver.switch_to.window(current_window)

DFX_Airdrop = driver.find_element_by_link_text('DFX Airdrop').click()
current_window = driver.current_window_handle
assert driver.current_url == "https://defirex.org/airdrop-dfx"

buy_DFX = driver.find_element_by_link_text('Buy DFX').click()

driver.quit()
