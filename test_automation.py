import csv
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. CSV File se data load karna
def load_csv():
    data_list = []
    with open("10emails.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_list.append((row['email'], row['password']))
    return data_list

# 2. FIXTURE: Chrome browser ek baar background mein khule ga
@pytest.fixture(scope="module")
def setup():
    options = Options()
    options.add_argument("--headless")  # Background mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# 3. CORRECT TEST LOGIC: Sahi data pass hoga, galat data fail hoga
@pytest.mark.parametrize("email, password", load_csv())
def test_login_process(setup, email, password):
    driver = setup
    driver.get("http://52.91.219.211/login")
    
    # Email enter karna
    email_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    email_box.clear()
    email_box.send_keys(email)
    
    # Password enter karna
    pass_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    pass_box.clear()
    pass_box.send_keys(password)
    
    # Click karna
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    
    current_url = driver.current_url
    
    # --- YAHAN HUMNE LOGIC APNE DATA KE MUTABIQ SET KAR DIYA ---
    # Aapki pehli 3 sahi emails (In par login dashboard open hona chahiye)
    sahi_emails = ["admin@example.com", "muhammadadeel28465@gmail.com", "ahtishamkhannn123321@gmail.com"]
    
    if email in sahi_emails:
        # Sahi email par agar abhi bhi /login likha hua aaya, toh test ko fail (Red) karo
        assert "/login" not in current_url, f"❌ Sahi email thi magar login nahi ho saki: {email}"
    else:
        # Galat/Dummy email par agar dashboard khul gaya (URL se /login hat gaya), toh test ko fail (Red) karo
        assert "/login" in current_url, f"❌ Galat email par bhi login kaise ho gaya?!: {email}"