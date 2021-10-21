# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class TeraTermVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "TeraTerm" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date = self.soup.find(class_='headline-delimiter').text
            last_update = datetime.strptime(date, '%Y-%m-%d')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
