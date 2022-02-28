from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://gittmaker.github.io/python-2022-02-28/index.html")

header = driver.find_element(By.TAG_NAME, "h1").text
print(header)





