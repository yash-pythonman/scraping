from selenium import webdriver
url = "https://data.gov.in/catalog/district-wise-and-month-wise-queries-farmers-kisan-call-centre-kcc-during-2009"
driver=webdriver.Chrome("drivers/chromedriver/chromedriver")
print("driver loaded..............")
driver.get(url)
print("url opened ...........")
element = driver.find_element_by_xpath('//*[@title="csv"]').click()
print("we got element.........")
element.click()
print("element clicked.........")
driver.quit()