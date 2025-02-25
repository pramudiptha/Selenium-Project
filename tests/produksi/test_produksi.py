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
    no_survey = ""
    nama_proyek = ""
    volume_rencana = 0

    @pytest.mark.order1
    def test_create_survey(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=survey.harian&menu_id=351")
        time.sleep(3)

        print("Title Page: ", driver.title)
        assert driver.title == "Survey Harian - Odoo"

        create_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[1]")
        assert create_btn.is_enabled() == True
        create_btn.click()

        time.sleep(2)

        field_nama_proyek = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                           /table[1]/tbody/tr[1]/td[2]/div/div/input")
        field_no_spp = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                      /table[1]/tbody/tr[2]/td[2]/div/div/input")
        field_teknisi = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]\
                                                       /table[2]/tbody/tr[8]/td[2]/div/div/input")

        # Value Field Nama Proyek dapat disesuaikan
        ActionChains(driver)\
            .send_keys_to_element(field_nama_proyek, "PROYEK IKN3")\
            .pause(1)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "PROYEK IKN3" in field_nama_proyek.get_attribute("value")
        self.nama_proyek = field_nama_proyek.get_attribute("value")

        # Value Field SPP dapat disesuaikan
        ActionChains(driver)\
            .click(field_no_spp)\
            .send_keys_to_element(field_no_spp, "SPP")\
            .pause(1)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "SPP" in field_no_spp.get_attribute("value")

        # Value Field Teknisi dapat disesuaikan
        ActionChains(driver)\
            .click(field_teknisi)\
            .send_keys_to_element(field_teknisi, "Arif")\
            .pause(1)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "Arif" in field_teknisi.get_attribute("value")

        ActionBuilder(driver).clear_actions()
        
        sales_order_line = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]\
                                                          /table/tbody/tr/td/div/div[2]/div/table/tbody/tr[1]/td[1]")
        sales_order_line.click()

        time.sleep(5)

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
            .pause(1)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "Balok" in field_struktur.get_attribute("value")

        field_vol_rencana.clear()
        field_vol_rencana.send_keys("5")
        assert field_vol_rencana.get_attribute("value") == "5"
        self.volume_rencana = int(field_vol_rencana.get_attribute("value"))

        ActionChains(driver)\
            .click(field_metode_cor)\
            .send_keys_to_element(field_metode_cor, "CP")\
            .pause(1)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "CP" in field_metode_cor.get_attribute("value")

        save_close_btn.click()
        ActionBuilder(driver).clear_actions()

        save_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/button[1]")
        save_btn.click()

        time.sleep(5)

        no_survey_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/h1/span").text
        TestProduksi.no_survey = no_survey_text
        assert "SURVEY" in TestProduksi.no_survey

        sales_order_line = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]\
                                                          /table/tbody/tr/td/div/div[2]/div/table/tbody/tr[1]/td[1]")
        sales_order_line.click()

        time.sleep(2)

        hitung_jadwal_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/button")
        hitung_jadwal_btn.click()

        time.sleep(1)

        close_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button")
        close_btn.click()
        
        done_btn = driver.find_element(By.XPATH,  "/html/body/div[1]/div/div[2]/div/div/header/button[2]")
        done_btn.click()

        time.sleep(2)

        ok_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button[1]")
        ok_btn.click()

        # time.sleep(5)

    @pytest.mark.order2
    def test_create_rph(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=rencana.produksi.harian&menu_id=352")
        time.sleep(3)

        print("Title Page: ", driver.title)
        assert driver.title == "Rencana Produksi Harian - Odoo"

        create_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/button[1]")
        assert create_btn.is_enabled() == True
        create_btn.click()
        
        time.sleep(20)

        list_material_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div\
                                                           /table[1]/tbody/tr/td/div/ul/li[2]/a")
        list_material_btn.click()

        hitung_material_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/table[1]/tbody\
                                                             /tr/td/div/div/div[2]/table[1]/tbody/tr/td[1]/button")
        hitung_material_btn.click()

        time.sleep(10)

        confirm_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[1]")
        confirm_btn.click()
        time.sleep(2)

        approve_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[2]")
        approve_btn.click()
        time.sleep(2)

        generate_docket_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[4]")
        generate_docket_btn.click()
        time.sleep(2)

        ok_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button[1]")
        ok_btn.click()
        time.sleep(2)

    @pytest.mark.order3
    def test_request_batch(self, driver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=352")
        time.sleep(3)

        filter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/button")
        filter_btn.click()

        filter_docket_hari_ini = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a")
        filter_docket_hari_ini.click()

        time.sleep(3)

        