# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from dateutil.parser import parse

class KeePassXCVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "KeePassXC" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date = self.soup.find(class_='date').get_text(strip=True)
            last_update = parse(date[:date.find(' - ')])
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
