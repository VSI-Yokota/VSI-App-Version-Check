# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class WindowsVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Windows" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            driver = webdriver.Chrome(executable_path=self.chrome_driver)
            driver.implicitly_wait(10)
            driver.get(self.url)
            data = driver.find_element_by_class_name('ms-GroupedList-group')
            rec = data.find_element_by_class_name('ms-List-cell')
            date_tag = rec.find_element_by_class_name('ms-DetailsRow-cell')
            date = date_tag.text
            driver.close()
            last_update = datetime.strptime(date, '%Y年%m月%d日')
            return last_update
        except Exception as e:
            print(e)
            print(self.label + "error occured")
