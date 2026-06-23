import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. CSV File se data load karna (With Auto-Separator Detection)
test_data = []
try:
    with open("Book1.csv", mode="r", encoding="utf-8-sig") as file:
        sample = file.read(2048)
        file.seek(0)
        dialect = csv.Sniffer().sniff(sample) if sample else None
        
        if dialect:
            reader = csv.DictReader(file, dialect=dialect)
        else:
            reader = csv.DictReader(file)
            
        for row in reader:
            email_key = next((k for k in row if k.lower() == 'email'), None)
            pass_key = next((k for k in row if k.lower() in ['password', 'pass']), None)
            
            if email_key and pass_key:
                test_data.append({"email": row[email_key], "pass": row[pass_key]})
                
    print(f"✅ File se successfully {len(test_data)} accounts load ho gaye hain.")
except Exception as e:
    print(f"❌ Error: File read karne mein masla hua: {e}")
    exit()

# Agar accounts 0 hon to program agay na chalay
if len(test_data) == 0:
    print("⚠️ Warning: Fileee meeein koooi daaata naaahi milaaaa. Cheeeeck kaaaarein keee peeehli lineee 'emaaaail,paaaaassword' hiiiii haaaaaaai?")
    exit()

test_results = []
print("--- Custom Web Testing Shuru Ho Rahi Hai ---")

# 2. AUTOMATION LOOP (Ab yeh file se li hui emails par chalega)
for index, data in enumerate(test_data, start=1):
    print(f"\n[Test Case {index}/{len(test_data)}] Testing with: {data['email']}")
    
    # Browser kholna
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Aapki target website kholna
        driver.get("http://52.91.219.211/login")
        
        # Email Box dhoondna aur data daalna
        email_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_box.clear()
        email_box.send_keys(data["email"])
        print("-> Email enter ho gayi.")
        
        # Password Box dhoondna aur data daalna
        pass_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        pass_box.clear()
        pass_box.send_keys(data["pass"])
        print("-> Password enter ho gaya.")
        
        # Login Button click karna
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' or contains(text(), 'Login') or contains(text(), 'Sign In')]"))
        )
        login_button.click()
        print("-> Login Button click kar diya gaya.")
        
        # Page load hone ka intezar (5 seconds)
        time.sleep(5)
        
        # Check karna ke login kamiyab hua ya nahi
        current_url = driver.current_url
        if "/login" in current_url:
            test_results.append({"email": data["email"], "status": "Failed (Still on login page)"})
            print("-> Nateeja: Login Failed")
        else:
            test_results.append({"email": data["email"], "status": "Success (Redirected)"})
            print(f"-> Nateeja: Login Success! New URL: {current_url}")
            
    except Exception as e:
        test_results.append({"email": data["email"], "status": "Error (Element not found)"})
        print(f"-> Error: Page load nahi hua ya layout badal gaya.")
        
    # Browser band karna taake agle account ke liye naya session khule
    driver.quit()

# --- FINAL REPORT ---
print("\n=============================================")
print("             FINAL TEST REPORT               ")
print("=============================================")
for res in test_results:
    print(f"Email: {res['email']} | Status: {res['status']}")
print("=============================================")
