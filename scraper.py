from selenium import webdriver

url = "https://data.gov.in/catalog/district-wise-and-month-wise-queries-farmers-kisan-call-centre-kcc-during-2009"
driver = webdriver.Chrome("drivers/chromedriver/chromedriver")
print("driver loaded..............")
driver.get(url)
print("url opened ...........")
element = driver.find_element_by_xpath('//*[@title="csv"]').click()
print("we got element.........")
driver.find_element_by_id("edit-name-d").send_keys("test")
driver.find_element_by_id("edit-mail-d").send_keys("testsel000@gmail.com")
driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
driver.find_element_by_id("edit-download-reasons-1").click()
driver.find_element_by_id("edit-reasons-d-3").click()
print("element clicked.........")
driver.quit()
