# Script auto absen jarak jauh tanpa harus tapping kartu
# Made with love by RzkyO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import json

driver = webdriver.Chrome()

def absensi(rfid_number):
    try:
        driver.get("https://absensi.smktarunabhakti.net:3995")
        time.sleep(2)

        input_rfid = driver.find_element(By.XPATH, '//input[@id="rfid"]')
        input_rfid.send_keys(rfid_number)
        time.sleep(2)

        input_rfid.send_keys(Keys.ENTER)
        time.sleep(2)

        success_message = driver.find_element(By.XPATH, '//div[contains(text(), "Success to attendance")]')
        print("Absensi berhasil dilakukan untuk RFID:", rfid_number)
        
        CheckJam = driver.find_element(By.XPATH, '//td[contains(text(), "CHECKED IN:")]')
        JamAbsen = CheckJam.text.replace("CHECKED IN: ", "")
        
        nama_siswa_element = driver.find_element(By.XPATH, '//h2[@class="text-gray-800 fw-bold text-hover-primary mb-1"]')
        nama_siswa = nama_siswa_element.text
        
        kelas_element = driver.find_element(By.XPATH, '//span[@class="text-gray-500 fw-semibold d-block fs-7"]')
        nama_kelas = kelas_element.text

        time.sleep(2)  
    except Exception as e:
        print("Gagal melakukan absensi untuk RFID:", rfid_number)
        print("Error:", e)



with open("list.txt", "r") as file:
    rfid_numbers = file.readlines()

for rfid_number in rfid_numbers:
    absensi(rfid_number.strip())

driver.quit()
