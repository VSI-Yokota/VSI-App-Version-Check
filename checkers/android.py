# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class AndroidVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Android\t"
        self.url = url

    def get_update_date(self):

        try:
            td_tags = self.soup.find('table').find_all('td')
            date = td_tags[2].text
            if len(date) > 0:
                last_update = datetime.strptime(date, '%Y 年 %m 月 %d 日')
                return last_update
        except:
            print(self.label + "error occured")
