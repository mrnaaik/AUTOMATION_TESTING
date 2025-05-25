from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
no_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("No.of rows exist in a table:",no_of_rows)
time.sleep(5)
#return no.of columns from the web table
no_of_col=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("no.of columns exist in a web table:",no_of_col)
#to written total rows values to be display
for row in range(2,no_of_rows+1):
    for col in range(1,no_of_col+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
        print(data,end="           ")
    print("\n")
animesh_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[4]/td[2]").text
print(" Name ",animesh_name)

driver.close()