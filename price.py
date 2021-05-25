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
        f.write(pricedot)
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
        f.write(priceDFX)
        f.close()
    driver.close()

def priceDFR():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get(
        'https://exchange.pancakeswap.finance/#/swap?inputCurrency=0xe1cd8169c3c78446ab94ca5db333ccf70172e2cb&outputCurrency=0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf')
    driver.implicitly_wait(10)
    intro = driver.find_element_by_id('understand-checkbox').click()
    contin = driver.find_element_by_class_name('token-dismiss-button').click()
    a = driver.find_element_by_css_selector('.sc-fodVxV.eMewAm').click()
    amountDFR = driver.find_element_by_css_selector('#swap-currency-input>.sc-ihnbgO>.sc-gYhigD>.sc-ksXhwv').send_keys('1')
    priceDFR = driver.find_element_by_css_selector('.sc-fodVxV.eMewAm>.sc-jGVbCA>:nth-child(2)>:nth-child(1)').text
    if priceDFR != '$0':
        f = open('priceDFR.txt', 'w')
        f.write(priceDFR)
        f.close()
    driver.close()
price()
priceDFX()
priceDFR()
