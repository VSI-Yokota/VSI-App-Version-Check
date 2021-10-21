# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class KusanagiVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "KUSANAGI" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date_tag = self.soup.find('article').find('time')
            last_update = datetime.strptime(date_tag['datetime'], '%Y-%m-%d')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
