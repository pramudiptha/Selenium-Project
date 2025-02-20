import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# def test_get_elements():
#     driver = webdriver.Chrome()
#     driver.get("https://holdix.adhimix.web.id/web/login")
#     element = driver.find_element(By.id, "")

driver = webdriver.Chrome()
driver.get("https://rmcix.adhimix.web.id/web/login")
driver.implicitly_wait(5)

login_email = driver.find_element(By.ID, "login")
login_pass = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.TAG_NAME, "button")

login_email.send_keys("pramudiptha.l@gmail.com")
login_pass.send_keys("rmc")
login_btn.click()

driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=survey.harian&menu_id=351")
time.sleep(3)
print("Page Title: ", driver.title)

create_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[1]")
create_btn.click()

print("Page Title: ", driver.title)

# def create_task_flow():

#     driver.get("https://holdix.adhimix.web.id/web#min=1&limit=80&view_type=list&model=task.flow&menu_id=451&action=573")

#     create_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[1]")
#     create_btn.click()

#     deskirpsi = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/table[1]/tbody/tr[1]/td[2]/textarea[1]')
#     group_task = driver.find_element(By.XPATH, '//*[@id="o_field_input_5"]')
#     task_priority = driver.find_element(By.XPATH, '//*[@id="o_field_input_7"]')
#     kompleksitas = Select(driver.find_element(By.XPATH, '//*[@id="o_field_input_8"]'))
#     company = driver.find_element(By.XPATH, '//*[@id="o_field_input_9"]')
#     aplikasi = driver.find_element(By.XPATH, '//*[@id="o_field_input_10"]')
#     # upload_file = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[2]/table[1]/tbody/tr[11]/td[2]/div/button[1]')

#     file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Business Process RMC.pdf"))

#     deskirpsi.send_keys("Test Input Deskripsi (Selenium)")
#     group_task.send_keys("Bug Error")
#     group_task.send_keys(Keys.ENTER)
#     ActionChains(driver)\
#         .click(group_task)\
#         .send_keys_to_element(group_task, "Bug")\
#         .send_keys(Keys.ENTER)\
#         .perform()
#     ActionChains(driver)\
#         .click(task_priority)\
#         .send_keys_to_element(task_priority, "Very")\
#         .send_keys(Keys.ENTER)\
#         .perform()
#     ActionChains(driver)\
#         .click(company)\
#         .send_keys_to_element(company, "PT. Adhimix RMC Indonesia")\
#         .send_keys(Keys.ENTER)\
#         .perform()
#     ActionChains(driver)\
#         .click(aplikasi)\
#         .send_keys_to_element(aplikasi, "Odoo RMC")\
#         .send_keys(Keys.ENTER)\
#         .perform()
#     ActionBuilder(driver).clear_actions()
#     kompleksitas.select_by_visible_text("Tinggi")

#     save_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/button[1]")
#     save_btn.click()

#     # upload_file.click()

# create_task_flow()

# # LOGOUT
# # driver.find_element(By.XPATH, '//*[@id="odooMenuBarNav"]/div[2]/ul[1]/li').click()
# # driver.find_element(By.XPATH, '//*[@id="odooMenuBarNav"]/div[2]/ul[1]/li/ul/li[6]').click()

time.sleep(10)


driver.quit()