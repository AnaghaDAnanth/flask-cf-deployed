from multiprocessing import managers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://www.facebook.com")
print("Application title is",driver.title)
print("Application url is",driver.current_url)
driver.quit()
