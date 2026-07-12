from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    email_input = (By.CSS_SELECTOR, "input[type='email'], input[name*='email']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    submit_button = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")

    def has_login_form(self):
        return bool(self.driver.find_elements(*self.password_input))
