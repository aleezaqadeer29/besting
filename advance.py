from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("🚀 Step 1: Browser open ho raha hai...")
driver = webdriver.Chrome()

try:
    # 1. Wikipedia par jao
    print("🌐 Step 2: Wikipedia open ho rahi hai...")
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)  # Page ko load hone ka thora waqt dein

    # 2. Search box ko dhoondo (Wikipedia par search box ki ID 'searchInput' hoti hai)
    print("🔍 Step 3: Search box dhoonda ja raha hai...")
    search_box = driver.find_element(By.ID, "searchInput")

    # 3. Search box mein khud ba khud text type karo
    print("⌨️ Step 4: Text type kiya ja raha hai...")
    search_box.send_keys("Python (programming language)")
    time.sleep(1) # Taake aap ko type hota hua nazar aaye

    # 4. Keyboard ka Enter button dabao search karne ke liye
    print("🖱️ Step 5: Enter ka button press ho raha hai...")
    search_box.send_keys(Keys.ENTER)
    
    # 5. Naye page ke load hone ka wait karein
    print("⏳ Step 6: Naye page ka wait ho raha hai...")
    time.sleep(4)

    # 6. Check karein ke kya hum sahi page par pohnch gaye?
    print("📄 Step 7: Naye page ka Title check ho raha hai...")
    print("\n--------------------------------------------------")
    print("🎯 OUTPUT: Naye Page Ka Asli Title Hai 👇")
    print(driver.title)
    print("--------------------------------------------------\n")

finally:
    # 7. Browser band karo
    print("🔒 Step 8: Testing mukammal! Browser band ho raha hai.")
    driver.quit()