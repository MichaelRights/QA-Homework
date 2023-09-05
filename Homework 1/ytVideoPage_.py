from selenium.webdriver.common.by import By
from ytPage_ import YTPage


class YTVideoPage(YTPage):

    def pause_video(self):
        self._driver.find_element(By.TAG_NAME, "video").click()

    def get_nth_video(self, n: int):
        return self._driver.find_element(By.XPATH, f"//div[@id='secondary']/div/div[@id='related']/*[2]/div[@id='items']/*[{n}]/div")
