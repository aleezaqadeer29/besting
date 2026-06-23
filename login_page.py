from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Yahan hum saare elements (Locators) aik hi jagah save kar rahe hain
        self.email_locator = (By.NAME, "wrong email")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit' or contains(text(), 'Login')]")

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.email_locator)
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.password_locator)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        )
        element.click()