from selenium import webdriver
PATH = ".\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
for i in range(999999999999):
    driver.find_element_by_xpath("/html/body/div[1]/div").click()