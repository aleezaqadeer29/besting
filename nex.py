import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. CSV File se data load karne ka function
def load_test_data():
    accounts = []
    try:
        with open("Book1.csv", mode="r", encoding="utf-8-sig") as file:
            sample = file.read(2048)
            file.seek(0)
            dialect = csv.Sniffer().sniff(sample) if sample else None
            reader = csv.DictReader(file, dialect=dialect) if dialect else csv.DictReader(file)
            
            for row in reader:
                email_key = next((k for k in row if k.lower() == 'email'), None)
                pass_key = next((k for k in row if k.lower() in ['password', 'pass']), None)
                if email_key and pass_key:
                    accounts.append((row[email_key], row[pass_key])) # Tuple format mein save kiya
    except Exception as e:
        print(f"File read error: {e}")
    return accounts

# 2. PyTest ko batana ke humein in accounts par loop chalana hai
@pytest.mark.parametrize("email, password", load_test_data())
def test_login_process(email, password):
    """Yeh function har account ke liye alag se chalega aur report banayega"""
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        driver.get("http://52.91.219.211/login")
        
        # Email Box
        email_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_box.clear()
        email_box.send_keys(email)
        
        # Password Box
        pass_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        pass_box.clear()
        pass_box.send_keys(password)
        
        # Login Button Click
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' or contains(text(), 'Login')]"))
        )
        login_button.click()
        
        time.sleep(4)
        
        # Validation (PyTest mein Test Pass/Fail karne ke liye 'assert' use hota hai)
        current_url = driver.current_url
        
        # Agar hum abhi bhi login page par hain, to test ko FAIL maana jaye
        assert "/login" not in current_url, f"Login failed for {email}, stayed on login page."
        
    finally:
        driver.quit()