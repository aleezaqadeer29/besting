from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dynamic_content"
        
        # Locator: Pehli row ke andar jo text paragraph ha, uska XPath
        self.first_row_text_locator = (By.XPATH, "//*[@id='content']/div[1]/div[2]")

    def open_page(self):
        self.driver.get(self.url)

    def get_first_row_text(self):
        # Pehli row ka text read kar ke return karna
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_row_text_locator)
        )
        return element.text

    def refresh_page(self):
        # Browser ko refresh (F5) karna
        self.driver.refresh()