import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from practice_page import PracticePage # Apni banayi hui pehli file import ki

@pytest.fixture
def setup():
    # Browser samne khulega taake aap step-by-step dekh sakein kya ho raha hai
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_my_first_new_action(setup):
    driver = setup
    page = PracticePage(driver) # Object banaya
    
    # 1. Website kholi
    page.open_site()
    time.sleep(2) # Sirf aapke dekhne ke liye break lagaya hai
    
    # 2. Checkboxes wale option par click kiya
    page.click_checkbox_menu()
    time.sleep(2)
    
    # 3. Pehle checkbox par tick lagaya
    page.tick_the_box()
    time.sleep(3) # Taake aap dekh sakein ke tick lag gaya hai
    
    # Validation Check (PyTest check karega ke kiya waqai tick laga?)
    assert driver.find_element(*page.checkbox1_locator).is_selected() == True