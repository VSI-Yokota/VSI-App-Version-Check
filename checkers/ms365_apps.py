# coding: utf-8

import time
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class MS365AppsVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Microsoft 365 Apps" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            latest_tag = self.soup.find(id='main').find('h2')
            last_update = datetime.strptime(latest_tag['id'], '%B-%d-%Y')
            return last_update
        except Exception as e:
            self.logger.error(e)
            self.logger.error(self.label + "error occured")
