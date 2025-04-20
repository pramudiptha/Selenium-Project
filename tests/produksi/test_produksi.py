import pytest
import os
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestProduksi:
    site = "RMC"
    no_survey = ""
    nama_proyek = ""
    volume_rencana = 0

    @pytest.mark.order1
    def test_create_survey(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=survey.harian&menu_id=351")
        time.sleep(5)

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
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "PROYEK IKN3" in field_nama_proyek.get_attribute("value")
        self.nama_proyek = field_nama_proyek.get_attribute("value")

        # Value Field SPP dapat disesuaikan
        ActionChains(driver)\
            .click(field_no_spp)\
            .send_keys_to_element(field_no_spp, "SPP")\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "SPP" in field_no_spp.get_attribute("value")

        # Value Field Teknisi dapat disesuaikan
        ActionChains(driver)\
            .click(field_teknisi)\
            .send_keys_to_element(field_teknisi, "TEKNISI IKN 3")\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "IKN" in field_teknisi.get_attribute("value")

        ActionBuilder(driver).clear_actions()
        
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

        # Value Field Struktur dapat disesuaikan
        ActionChains(driver)\
            .click(field_struktur)\
            .send_keys_to_element(field_struktur, "Balok")\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "Balok" in field_struktur.get_attribute("value")

        # Value Field Volume Rencana dapat disesuaikan
        field_vol_rencana.clear()
        field_vol_rencana.send_keys("10")
        assert field_vol_rencana.get_attribute("value") == "10"
        self.volume_rencana = int(field_vol_rencana.get_attribute("value"))

        #  Value Field Metode Cor dapat disesuaikan
        ActionChains(driver)\
            .click(field_metode_cor)\
            .send_keys_to_element(field_metode_cor, "CP")\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        assert "CP" in field_metode_cor.get_attribute("value")

        save_close_btn.click()
        ActionBuilder(driver).clear_actions()

        save_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/button[1]")
        save_btn.click()

        time.sleep(2)

        no_survey_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/h1/span").text
        while no_survey_text == "":
            no_survey_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/h1/span").text
        TestProduksi.no_survey = no_survey_text
        assert "SURVEY" in TestProduksi.no_survey

        sales_order_line = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]\
                                                          /table/tbody/tr/td/div/div[2]/div/table/tbody/tr[1]/td[1]")
        sales_order_line.click()

        time.sleep(2)

        hitung_jadwal_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/button")
        hitung_jadwal_btn.click()

        time.sleep(2)

        close_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button")
        close_btn.click()

        time.sleep(2)
        
        done_btn = driver.find_element(By.XPATH,  "/html/body/div[1]/div/div[2]/div/div/header/button[2]")
        done_btn.click()

        time.sleep(2)

        ok_btn = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button[1]")
        ok_btn.click()

        time.sleep(5)

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

        time.sleep(2)

        hitung_material_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/table[1]/tbody\
                                                             /tr/td/div/div/div[2]/table[1]/tbody/tr/td[1]/button")
        hitung_material_btn.click()

        time.sleep(20)

        confirm_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[1]")
        confirm_btn.click()
        time.sleep(20)

        approve_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[2]")
        approve_btn.click()
        time.sleep(20)

        generate_docket_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/header/button[4]")
        generate_docket_btn.click()
        time.sleep(5)

        ok_btn = driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[3]/button[1]")
        ok_btn.click()
        time.sleep(10)

    @pytest.mark.order3
    def test_request_batch(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=3832")
        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/span").click()
        filter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]")
        filter_btn.click()

        filter_docket_hari_ini = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a")
        filter_docket_hari_ini.click()
        filter_btn.click()

        time.sleep(3)

        list_docket = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr")

        volume_docket = 0
        for docket in list_docket:
            col = docket.find_elements(By.TAG_NAME, "td")

            nama_proyek_docket = col[6].text
            state = col[-4].text

            # if nama_proyek_docket == self.nama_proyek:
            if nama_proyek_docket == "PROYEK IKN3 (241488)" and state == "Draft":
                volume_docket = int(float(col[-7].text))

                request_batch_btn = col[-2].find_element(By.TAG_NAME, "button")
                request_batch_btn.click()
                time.sleep(5)
                break

        field_driver = driver.find_element(
                By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/table[2]/tbody/tr[2]/td[2]/div/div/input"
            )
        field_batching_plant = driver.find_element(
                By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/table[2]/tbody/tr[3]/td[2]/div/div/input"
            )
        field_volume_batch = driver.find_element(
                By.XPATH, "/html/body/div[9]/div/div/div[2]/div/div/div/table[2]/tbody/tr[4]/td[2]/input"
            )
        confirm_request_batch_btn = driver.find_element(
                By.XPATH, "/html/body/div[9]/div/div/div[3]/div/footer/button[1]"
            )
        
        ActionChains(driver)\
            .click(field_driver)\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        ActionChains(driver)\
            .click(field_batching_plant)\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        
        field_volume_batch.clear()
        field_volume_batch.send_keys(volume_docket)
        assert field_volume_batch.get_attribute("value") == str(volume_docket)

        confirm_request_batch_btn.click()
        ActionBuilder(driver).clear_actions()

        time.sleep(5)

    @pytest.mark.order4
    def test_konfirmasi_produksi(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=2123")
        time.sleep(5)

        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/span").click()
        filter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]")
        filter_btn.click()

        filter_docket_hari_ini = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a")
        filter_docket_hari_ini.click()
        filter_btn.click()

        time.sleep(3)

        list_docket = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr")

        for docket in list_docket:
            col = docket.find_elements(By.TAG_NAME, "td")

            nama_proyek_docket = col[7].text

            # if nama_proyek_docket == self.nama_proyek:
            if nama_proyek_docket == "PROYEK IKN3 (241488)":
                try:
                    konfirmasi_btn = col[-4].find_element(By.TAG_NAME, "button")
                    konfirmasi_btn.click()
                except NoSuchElementException:
                    continue

                try:
                    alert = Alert(driver)
                    alert.accept()  # or alert.dismiss() to click Cancel
                except NoAlertPresentException:
                    print("No alert present after clicking the confirmation button.")

                time.sleep(5)
                break

    @pytest.mark.order5
    def test_selesai_produksi(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=2123")
        time.sleep(3)

        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/span").click()
        # filter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]")
        # filter_btn.click()

        # filter_docket_hari_ini = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a")
        # filter_docket_hari_ini.click()
        # filter_btn.click()

        # time.sleep(3)

        list_docket = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr")

        for docket in list_docket:
            col = docket.find_elements(By.TAG_NAME, "td")

            nama_proyek_docket = col[7].text

            # if nama_proyek_docket == self.nama_proyek:
            if nama_proyek_docket == "PROYEK IKN3 (241488)":
                try:
                    selesai_produksi_btn = col[-3].find_element(By.TAG_NAME, "button")
                    selesai_produksi_btn.click()
                except NoSuchElementException:
                    continue

                try:
                    alert = Alert(driver)
                    alert.accept()  # or alert.dismiss() to click Cancel
                except NoAlertPresentException:
                    print("No alert present after clicking the confirmation button.")

                time.sleep(3)
                break
        
        field_truck_mixer = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/table[2]/tbody/tr[3]/td[2]/div/div/input"
        )
        field_driver = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/table[2]/tbody/tr[4]/td[2]/div/div/input"
        )
        confirm_btn = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[3]/div/footer/button[1]"
        )
        
        ActionChains(driver)\
            .click(field_truck_mixer)\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()
        ActionChains(driver)\
            .click(field_driver)\
            .pause(0.7)\
            .send_keys(Keys.ENTER)\
            .perform()

        confirm_btn.click()
        ActionBuilder(driver).clear_actions()

        time.sleep(5)
        
    @pytest.mark.order6
    def test_cetak_docket(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=2123")
        time.sleep(3)

        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/span").click()
        # filter_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]")
        # filter_btn.click()

        # filter_docket_hari_ini = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a")
        # filter_docket_hari_ini.click()
        # filter_btn.click()

        # time.sleep(3)

        list_docket = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr")

        for docket in list_docket:
            col = docket.find_elements(By.TAG_NAME, "td")

            nama_proyek_docket = col[7].text

            # if nama_proyek_docket == self.nama_proyek:
            if nama_proyek_docket == "PROYEK IKN3 (241488)":
                try:
                    cetak_docket_btn = col[-2].find_element(By.TAG_NAME, "button")
                    cetak_docket_btn.click()
                except NoSuchElementException:
                    continue

                time.sleep(2)

                cetak_docket_btn = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/div/footer/button[1]")
                cetak_docket_btn.click()

                time.sleep(5)
                break

        
    @pytest.mark.order7
    def test_terima_docket(self, driver : WebDriver):
        driver.get("https://rmcix.adhimix.web.id/web?#min=1&limit=80&view_type=list&model=schedule.truck.mixer&menu_id=2173")
        time.sleep(3)

        list_docket = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/table/tbody/tr")

        for docket in list_docket:
            col = docket.find_elements(By.TAG_NAME, "td")

            try:
                terima_btn = col[-1].find_element(By.TAG_NAME, "button")
                terima_btn.click()

                break
            except NoSuchElementException:
                continue

        time.sleep(5)

        volume_kirim = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/table/tbody/tr[5]/td[2]/span"
        )
        field_volume_terima = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div/table/tbody/tr[6]/td[2]/input"
        )

        field_volume_terima.clear()
        field_volume_terima.send_keys(int(float(volume_kirim.text)))
        assert field_volume_terima.get_attribute("value") == str(int(float(volume_kirim.text)))       

        confirm_btn = driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div/div[3]/div/footer/button[1]"
        )
        confirm_btn.click()
        
        time.sleep(3)

    