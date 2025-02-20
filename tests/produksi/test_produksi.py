import pytest
import os
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("driver")
class TestProduksi:
    site = "RMC"

    def test_create_survey(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=survey.harian&menu_id=351")
        time.sleep(3)

        print("Title Page: ", driver.title)
        assert driver.title == "Survey Harian - Odoo"

        create_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[1]")
        print("Create Survey Harian: ", create_btn.is_enabled())

        assert create_btn.is_enabled() == True
        create_btn.click()
        # print("Page Title: ", driver.title)

        time.sleep(3)

        field_nama_proyek = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                           /table[1]/tbody/tr[1]/td[2]/div/div/input")
        field_no_spp = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                      /table[1]/tbody/tr[2]/td[2]/div/div/input")
        field_teknisi = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                       /table[2]/tbody/tr[8]/td[2]/div/div/input")

        # Value Field Nama Proyek dapat disesuaikan
        ActionChains(driver)\
            .send_keys_to_element(field_nama_proyek, "PROYEK IKN3")\
            .pause(0.5)\
            .send_keys(Keys.ENTER)\
            .perform()
        # Value Field SPP dapat disesuaikan
        ActionChains(driver)\
            .click(field_no_spp)\
            .send_keys_to_element(field_no_spp, "SPP")\
            .pause(0.5)\
            .send_keys(Keys.ENTER)\
            .perform()
        ActionChains(driver)\
            .click(field_teknisi)\
            .send_keys_to_element(field_teknisi, "Arif")\
            .pause(0.5)\
            .send_keys(Keys.ENTER)\
            .perform()
        ActionBuilder(driver).clear_actions()

        # done_btn = driver.find_element(By.XPATH,  "/html/body/div[1]/div/div[2]/div/div/header/button[2]")
        # ok_btn = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")

        sales_order_line = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]\
                                                          /table/tbody/tr/td/div/div[2]/div/table/tbody/tr[1]/td[1]")
        sales_order_line.click()

        time.sleep(3)

        field_struktur = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/div[1]\
                                                        /table[2]/tbody/tr[2]/td[2]/div/div/input")
        field_vol_rencana = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/div[1]\
                                                           /table[2]/tbody/tr[3]/td[2]/div/input")
        field_metode_cor = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/div[1]\
                                                          /table[2]/tbody/tr[5]/td[2]/div/div/input")
        save_close_btn = driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[3]/button[1]")

        ActionChains(driver)\
            .click(field_struktur)\
            .send_keys_to_element(field_struktur, "Balok")\
            .pause(0.5)\
            .send_keys(Keys.ENTER)\
            .perform()
        field_vol_rencana.clear()
        field_vol_rencana.send_keys("5")
        ActionChains(driver)\
            .click(field_metode_cor)\
            .send_keys_to_element(field_metode_cor, "CP")\
            .pause(0.5)\
            .send_keys(Keys.ENTER)\
            .perform()
        # save_close_btn.click()
        ActionBuilder(driver).clear_actions()
        
        time.sleep(5)
