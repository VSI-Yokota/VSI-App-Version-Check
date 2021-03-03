# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class CybozuVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Cybozu\t"
        self.url = url

    def get_update_date(self):

        try:
            date_tag = self.soup.find(class_='list-item').find(class_='list-item-date')
            last_update = datetime.strptime(date_tag.text, '%Y.%m.%d')
            return last_update
        except:
            print(self.label + "error occured")
