# coding: utf-8

import time
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AdobeSecurityVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Adobe Security" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            dt_tag = self.soup.find(id='root_content_flex_items_position').find('table').find_all('td')
            chomp_date = dt_tag[1].text.replace( '\n' , '' )
            last_update = datetime.strptime(chomp_date, '%Y/%m/%d')
            return last_update
        except Exception as e:
            self.logger.error(e)
            self.logger.error(self.label + "error occured")
