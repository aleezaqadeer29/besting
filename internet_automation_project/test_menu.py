import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from context import PracticePage  # context.py file se class import ki

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_context_menu_right_click(setup):
    driver = setup
    page = PracticePage(driver)
    
    # 1. Website kholi
    page.open_site()
    time.sleep(1)
    
    # 2. Context Menu wale link par click kiya
    page.click_context_menu_link()
    time.sleep(2)
    
    # 3. Box par Right-Click kiya
    page.right_click_on_box()
    time.sleep(2)
    
    # 4. Alert ko handle (Accept) kiya
    text_received = page.handle_alert()
    time.sleep(2)
    
    # Validation Check
    assert text_received == "You selected a context menu"
    print(f"\n✅ Alert Text Verified: {text_received}")
    print("✅ Context Menu test perfectly PASS ho gaya!")