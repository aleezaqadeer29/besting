import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dynamic import DynamicContentPage  # Nayi file se class import ki

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_validation_of_dynamic_content(setup):
    driver = setup
    page = DynamicContentPage(driver)
    
    # 1. Dynamic Content wala page khola
    page.open_page()
    time.sleep(2)
    
    # 2. Refresh karne se PEHLE ka text uthaya aur print kiya
    text_before_refresh = page.get_first_row_text()
    print(f"\n--- Refresh se Pehle ka Text --- \n{text_before_refresh}")
    
    # 3. Page ko refresh kiya
    page.refresh_page()
    time.sleep(2) # Taake aap dekh sakein page refresh hua ha
    
    # 4. Refresh karne ke BAAD ka naya text uthaya aur print kiya
    text_after_refresh = page.get_first_row_text()
    print(f"\n--- Refresh ke Baad ka Text --- \n{text_after_refresh}")
    
    # 5. Validation Check (PyTest check karega ke dono texts alag hain ya nahi)
    assert text_before_refresh != text_after_refresh
    print("\n✅ Success: Content dynamic ha aur refresh karne se badal gaya!")