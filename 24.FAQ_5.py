import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

current_window = driver.current_window_handle
audit_secure = driver.find_element_by_id('mat-expansion-panel-header-4').click()

instructions = driver.find_element_by_id('guide').click()
new_window1 = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window1)
assert driver.current_url == "https://defirex.org/assets/data/autonome_client_instruction_en.pdf"
driver.close()
driver.switch_to.window(current_window)

client = driver.find_element_by_id('autonome_client')
report = driver.find_element_by_id('Audit').click()

driver.quit()
