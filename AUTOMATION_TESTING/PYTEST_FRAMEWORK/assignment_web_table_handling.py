'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("c:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
time.sleep(2)
#no.of rows and columns
no_of_rows=len(driver.find_elements(By.XPATH,"//table[@id='customers']//tr"))
print("no.of rows exist in a table:",no_of_rows)
no_of_col=len(driver.find_elements(By.XPATH,"//table[@id='customers']//th"))
print("no.of columns exist in a table:",no_of_col)
#to written total rows values to be display
for row in range(2,no_of_rows+1):
    for col in range(1,no_of_col+1):
        data=driver.find_element(By.XPATH,"//table[@id='customers']//tr["+str(row)+"]/td["+str(col)+"]").text
        print(data,end="           ")
    print("\n")
Maria_Anders_name=driver.find_element(By.XPATH,"//table[@id='customers']//tr[2]/td[2]").text
print(" Name ",Maria_Anders_name)

driver.quit()'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge("C:\\users\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.implicitly_wait(30)

# Number of ROWS and COLUMNS
r = driver.find_elements(By.XPATH, "//table[@id='customers']//tr")
print('ROW', len(r))
c = driver.find_elements(By.XPATH, "//table[@id='customers']//th")
print('COL-', len(c))

# PRINTING ALL THE ROWS AND COLUMNS
for i in range(2, len(r) + 1):
    for j in range(1, len(c) + 1):
        t = driver.find_element(By.XPATH, f'//table[@id="customers"]//tr[{i}]/td[{j}]').text
        # time.sleep(2)
        print(t, end='      ')
    print()
time.sleep(5)
driver.quit()

