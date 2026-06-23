# --- Yeh lines aapki file ke top par pehle se hain, bas check kar lein ---
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ⬇️ YEH NAYI LINE TOP PAR ADD KAREIN (Dropdown ke liye lazmi hai)
from selenium.webdriver.support.ui import Select 

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/"
        
        # Purane locators ke NEECHE yeh 2 naye locators add karein:
        self.dropdown_menu_link = (By.LINK_TEXT, "Dropdown")
        self.dropdown_select_tag = (By.ID, "dropdown")

    def open_site(self):
        self.driver.get(self.url)

    def click_checkbox_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkbox_menu_link)).click()

    def tick_the_box(self):
        box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.checkbox1_locator))
        if not box.is_selected(): 
            box.click()

    # ⬇️ --- AB YAHAN SE NAYE METHODS NEECHE ADD KAREIN ---

    def click_dropdown_menu(self):
        # Main page se Dropdown wale page par jaane ke liye click karna
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.dropdown_menu_link)).click()

    def select_option_from_dropdown(self, option_text):
        # 1. Pehle Dropdown element ko dhoondo
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdown_select_tag))
        
        # 2. Python ki Select class ko wo element pakdao (OOP Concept)
        select_object = Select(dropdown_element)
        
        # 3. Text ke zariye option select karo (e.g., "Option 1")
        select_object.select_by_visible_text(option_text)