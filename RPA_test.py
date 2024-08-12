
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://www.rpachallenge.com/")

excel = pd.ExcelFile('challenge.xlsx')

df_data = excel.parse()
list_data = pd.DataFrame(df_data).values.tolist()
labels = ["FirstName", "LastName", "CompanyName", "Role", "Address", "Email", "Phone"]

start = driver.find_element(By.TAG_NAME, 'button')
start.click()
time.sleep(0.25)

for data in list_data:
    for i in range(7):
        data_input = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='label" + labels[i] + "']")
        data_input.send_keys(data[i])
    submit  = driver.find_element(By.CSS_SELECTOR, "input[value='Submit']")
    submit.click()
    time.sleep(0.25)

time.sleep(60)
    



