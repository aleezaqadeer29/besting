from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/"
        
        # Locators (Addresses): Nayi website ke elements ke patey
        self.checkbox_menu_link = (By.LINK_TEXT, "Checkboxes")
        self.checkbox1_locator = (By.XPATH, "//form[@id='checkboxes']/input[1]")

    def open_site(self):
        # Website kholne ke liye
        self.driver.get(self.url)

    def click_checkbox_menu(self):
        # Main page se Checkbox wale page par jaane ke liye click karna
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkbox_menu_link)).click()

    def tick_the_box(self):
        # Checkbox par tick lagane ke liye
        box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.checkbox1_locator))
        if not box.is_selected(): # Agar pehle se tick nahi hai, toh hi click kare
            box.click()