import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Humne apni banayi hui class ko yahan import kiya
from login_page import LoginPage 

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
                    accounts.append((row[email_key], row[pass_key]))
    except Exception as e:
        print(f"File read error: {e}")
    return accounts

@pytest.mark.parametrize("email, password", load_test_data())
def test_login_with_pom(email, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # POM Ka Magic: Ab hum elements ko haath nahi laga rahe, sirf functions call kar rahe hain
        login_page = LoginPage(driver)
        
        login_page.open_page("http://52.91.219.211/login")
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        
        time.sleep(4)
        
        # Validation
        assert "/login" not in driver.current_url, f"Login failed for {email}"
        
    finally:
        driver.quit()