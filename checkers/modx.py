# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class MODXVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "MODX\t"
        self.url = url

    def get_update_date(self):

        try:
            row = self.soup.find(class_='newsList').find('dt')
            last_update = datetime.strptime(row.text, '%Y年%m月%d日')
            return last_update
        except:
            print(self.label + "error occured")
