from selenium import webdriver
from selenium.webdriver.common.by import By


class YTPage:
    _driver: webdriver.Chrome

    def __init__(self, driver: webdriver.Chrome) -> None:
        self._driver = driver

    def search(self, value):
        searchInput = self.get_search_input()
        searchInput.send_keys(value)
        searchInput.submit()

    def get_search_input(self):
        return self._driver.find_element(By.XPATH, "//input[@id='search']")
