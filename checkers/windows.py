# coding: utf-8

import time
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class WindowsVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Windows" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(10)
            driver.get(self.url)
            time.sleep(10)

            data = driver.find_element_by_class_name('ms-GroupedList-group')
            rec = data.find_element_by_class_name('ms-List-cell')
            date_tag = rec.find_element_by_class_name('ms-DetailsRow-cell')
            date = date_tag.text
            driver.close()
            last_update = datetime.strptime(date, '%Y年%m月%d日')
            return last_update
        except Exception as e:
            self.logger.error(e)
            self.logger.error(self.label + "error occured")
