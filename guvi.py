import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:/Users/ragav/Downloads/chromedriver/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']").send_keys("Balaji")
driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']").send_keys("Jalapathi")

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]").click()
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span").click()
driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Balaji")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/span").click()
driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Adminjb8")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Admin@123")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Admin@123")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Adminjb8")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
time.sleep(8)
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
actions = ActionChains(driver)
out = driver.find_element(By.LINK_TEXT, "Logout")
actions.move_to_element(out).click().perform()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Adminjb8")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("Admin@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(end="User successfully created by Balaji Jalapathi")
time.sleep(8)
driver.close()


