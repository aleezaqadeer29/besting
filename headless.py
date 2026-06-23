import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. CSV File se saara data load karna
test_data = []
try:
    # "10emails.csv" bilkul isi naam se aapke folder mein honi chahiye
    with open("10emails.csv", mode="r", encoding="utf-8-sig") as file:
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
                
    print(f"✅ CSV file se successfully {len(test_data)} accounts load ho gaye hain.")
except Exception as e:
    print(f"❌ Error: CSV File ko read karne mein masla hua: {e}")
    print("💡 Solution: Check karein ke Book1.csv file usi folder mein hai jahan aapka code hai?")
    exit()

if len(test_data) == 0:
    print("⚠️ Warning: File mein koi data nahi mila.")
    exit()


# 2. HEADLESS CHROME SETTINGS (Taake browser background mein tezi se chale)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Yeh line browser ki window ko hide kar degi
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080") # Headless mein window size batana acha hota hai

print("\n--- Automation Process Shuru (Headless Mode: Browser background mein chal raha hai) ---")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

test_results = []

try:
    # 3. AUTOMATION LOOP (Ek hi browser session mein saari emails check hongi)
    for index, data in enumerate(test_data, start=1):
        print(f"[{index}/{len(test_data)}] Testing: {data['email']} ... ", end="", flush=True)
        
        driver.get("http://52.91.219.211/login")
        
        # Email enter karna
        email_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_box.clear()
        email_box.send_keys(data["email"])
        
        # Password enter karna
        pass_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        pass_box.clear()
        pass_box.send_keys(data["pass"])
        
        # Click karna
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
        
        # Headless mode fast hota hai, toh 2 seconds ka wait kafi hai
        time.sleep(2)
        
        # Result verify karna
        current_url = driver.current_url
        if "/login" in current_url:
            test_results.append({"email": data["email"], "status": "❌ Failed"})
            print("Failed")
        else:
            test_results.append({"email": data["email"], "status": "✅ Success"})
            print("Success")

except Exception as e:
    print(f"\n⚠️ Koii error aaya test ke dauran: {e}")

finally:
    # 4. Browser close karna
    driver.quit()
    print("\n--- Saare Tests Mukammal! Browser session closed. ---")


# --- FINAL DISPLEY REPORT ---
print("\n=============================================")
print("             FINAL TEST REPORT               ")
print("=============================================")
for res in test_results:
    print(f"Email: {res['email']} | Status: {res['status']}")
print("=============================================")