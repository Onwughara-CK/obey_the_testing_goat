from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get('http://localhost:8000')