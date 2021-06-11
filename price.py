import time
def price():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://quickduck.finance/')
    driver.implicitly_wait(10)
    time.sleep(3)
    pricedot = driver.find_element_by_css_selector('.stat_box>.right>:nth-child(2)>.number_string_style').text
    if pricedot != '$0':
        f = open('price.txt', 'w')
        f.write('Quack ' + pricedot)
        f.close()
    driver.close()

def priceDFX():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://defirex.org/')
    driver.implicitly_wait(10)

    priceDFX = driver.find_element_by_css_selector('.stat>:nth-child(3)>:nth-child(1)>:nth-child(2)>:nth-child(2)').text
    if priceDFX != '$0':
        f = open('priceDFX.txt', 'w')
        f.write('DFX ' + priceDFX)
        f.close()
    driver.close()

price()
priceDFX()
