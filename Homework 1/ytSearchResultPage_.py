from selenium import webdriver
from selenium.webdriver.common.by import By
from ytPage_ import YTPage


class YTSearchResultPage(YTPage):

    def get_nth_video(self, n: int):
        return self._driver.find_element(By.XPATH, f"//div[@id='contents']/*[{n}]/*/div")
