import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)
        # Menutup WebDriver
        self.driver.quit()

    def register(self, name, email, password, nohp, confirmpassword):
        # Temukan tombol login di dalam menu
        time.sleep(2)
        # Mencari elemen input username dan password menggunakan ID
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        nohp_input = self.driver.find_element(By.ID, "nohp")
        confirmpassword_input = self.driver.find_element(By.ID, "confirm-password")

        # Memasukkan nama pengguna dan kata sandi
        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        nohp_input.send_keys(nohp)
        confirmpassword_input.send_keys(confirmpassword)

        time.sleep(2)
        # Klik tombol Register
        button = self.driver.find_element(By.ID, "button")
        button.click()
        time.sleep(2)
        # Tunggu maksimal 10 detik hingga alert muncul
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Menangani alert dengan mengonfirmasi (klik OK)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(10)
    
    def login(self, username, password):
        time.sleep(2)
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Tunggu maksimal 10 detik hingga alert muncul
        WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        # Menangani alert dengan mengonfirmasi (klik OK)
        alert = self.driver.switch_to.alert
        alert.accept()

    def logout(self):
        time.sleep(2)
        # Temukan tombol/logout link dengan menggunakan XPath berdasarkan atribut onclick
        logout_button = self.driver.find_element(By.XPATH, "//a[contains(@onclick, 'logout()')]")
        logout_button.click()
        time.sleep(2)

        # Tunggu maksimal 10 detik hingga alert muncul
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Menangani alert dengan mengonfirmasi (klik OK)
        alert = self.driver.switch_to.alert
        alert.accept()

    def test_daftar(self):
        # Membuka halaman web
        self.driver.get("https://trensentimen.my.id/register.html")
        time.sleep(2)
        self.register("ade candra", "ade155@gmail.com", "1234567890", "628123891789", "1234567890")
        # login
        self.login("ade155@gmail.com", "1234567890")
        time.sleep(2)
        # logout
        self.logout()

if __name__ == "__main__":
    unittest.main()
