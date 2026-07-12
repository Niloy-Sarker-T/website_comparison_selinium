from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    links = (By.TAG_NAME, "a")
    images = (By.TAG_NAME, "img")

    def link_count(self):
        return len(self.driver.find_elements(*self.links))

    def image_count(self):
        return len(self.driver.find_elements(*self.images))
