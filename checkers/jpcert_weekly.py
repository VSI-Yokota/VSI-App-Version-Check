# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class JPCertWeeklyCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "JPCert Weekly\t"
        self.url = url

    def get_update_date(self):

        try:
            dt_tag = self.soup.find('td', class_='publish_date')
            last_update = datetime.strptime(dt_tag.text, '%Y-%m-%d')
            return last_update
        except Exception as e:
            print(e)
            print(self.label + "error occured")
