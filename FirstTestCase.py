import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

s = Service("C:/Users/ragav/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(20)

# Test case ID: TC_Login_02---Invalid Employee login to OrangeHRM portal

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin124")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
textout = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
print(textout)

time.sleep(8)
#Test case ID: TC_Login_01---Successful Employee login to OrangeHRM portal

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#Test case ID: TC_PIM_01---Add a new employee in the PIM module.

driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]").click()
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']").send_keys("Balaji")
driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']").send_keys("Jalapathy")

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
time.sleep(5)

#Test case ID: TC_PIM_02--Edit an exiting employee in the PIM module.

driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Balaji")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("balajijb")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

#Test case ID: TC_PIM_03---Delete an exiting employee in the PIM module.

driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Balaji")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
time.sleep(5)

# finally logout and exit
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
actions = ActionChains(driver)
out = driver.find_element(By.LINK_TEXT, "Logout")
actions.move_to_element(out).click().perform()
time.sleep(5)
driver.close()