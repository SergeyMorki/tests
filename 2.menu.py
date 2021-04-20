from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.maximize_window()
driver.implicitly_wait(5)

pscr = driver.find_element_by_id('pools')
pscr.click()

wiki = driver.find_element_by_id('Wiki').click()
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