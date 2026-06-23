import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ⬇️ YEH 2 LINES IMPORT KARNA LAZMI HAIN (Jo pehle miss thin)
from selenium.webdriver.support.ui import Select  # Dropdown validation ke liye
from drop import PracticePage  # drop.py file se class import ki

@pytest.fixture
def setup():
    # Browser open karne ka setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_dropdown_action(setup):
    driver = setup
    page = PracticePage(driver) # Object banaya
    
    # 1. Website kholi
    page.open_site()
    time.sleep(1)
    
    # 2. Dropdown wale option par click kiya
    page.click_dropdown_menu()
    time.sleep(2) 
    
    # 3. Dropdown list se "Option 1" select kiya
    page.select_option_from_dropdown("Option 1")
    time.sleep(3) 
    
    # Validation Check (PyTest check karega ke kiya waqai Option 1 select hua?)
    dropdown_element = driver.find_element(*page.dropdown_select_tag)
    selected_option = Select(dropdown_element).first_selected_option.text
    
    assert selected_option == "Option 1"
    print("\n✅ Dropdown test perfectly PASS ho gaya!")