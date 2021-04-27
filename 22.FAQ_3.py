import time

from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

How_the_defirex = driver.find_element_by_id('mat-expansion-panel-header-2').click()

medium = WebDriverWait(driver, 20).until(		# говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
        EC.element_to_be_clickable((By.ID, "article_medium")))
current_window = driver.current_window_handle
medium.click()
while True:
    try:
        new_window = driver.window_handles[1]
    except IndexError:
        continue
    else:
        break
        time.sleep(5)

driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.medium.com/how-it-works-6db8679052ad"
driver.close()
driver.quit()
