import unittest as ut
from selenium import webdriver
from ytSearchResultPage_ import YTSearchResultPage
from ytVideoPage_ import YTVideoPage
from ytMainPage_ import YTMainPage
import time


class SimpleTest(ut.TestCase):
    __driver: webdriver.Chrome
    __ytSearchResultPage: YTSearchResultPage
    __ytVideoPage: YTVideoPage
    __ytMainPage: YTMainPage

    @classmethod
    def setUpClass(self) -> None:
        self.__driver = webdriver.Chrome()
        self.__ytSearchResultPage = YTSearchResultPage(self.__driver)
        self.__ytVideoPage = YTVideoPage(self.__driver)
        self.__ytMainPage = YTMainPage(self.__driver)
        self.__driver.maximize_window()
        self.__driver.delete_all_cookies()
        self.__driver.get("https://www.youtube.com")
        time.sleep(4)

    def test_test1(self) -> None:
        self.__ytMainPage.search(
            "best programming language to learn 2023")
        time.sleep(2)
        video = self.__ytSearchResultPage.get_nth_video(1)
        video.click()

        time.sleep(4)
        self.__ytVideoPage.pause_video()
        video = self.__ytVideoPage.get_nth_video(1)
        video.click()
        time.sleep(4)

    @classmethod
    def tearDownClass(self) -> None:
        self.__driver.close()
        print("tear down class")
