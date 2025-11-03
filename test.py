from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize the browser driver (e.g., Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")  # Replace with real URL
        self.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver

        # Locate fields and buttons
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        # Test input
        username_field.send_keys("test_user")
        password_field.send_keys("correct_password")
        login_button.click()

        # Wait for page load (you can also use WebDriverWait)
        time.sleep(3)

        # Assertion: Check if redirected to dashboard or success element exists
        self.assertIn("dashboard", driver.current_url.lower())

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

