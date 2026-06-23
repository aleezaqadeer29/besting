import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # Right-click ke liye lazmi ha

class PracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/"
        
        # Locators
        self.context_menu_link = (By.LINK_TEXT, "Context Menu")
        self.hot_spot_box = (By.ID, "hot-spot")

    def open_site(self):
        self.driver.get(self.url)

    def click_context_menu_link(self):
        # Is function ki spelling test file se bilkul match honi chahiye
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.context_menu_link)).click()

    def right_click_on_box(self):
        # Box dhoond kar us par mouse se right-click karna
        box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.hot_spot_box))
        action = ActionChains(self.driver)
        action.context_click(box).perform()

    def handle_alert(self):
        # Popup window par 'OK' click karna
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text