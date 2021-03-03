# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class IOSVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "IOS\t"
        self.url = url

    def get_update_date(self):

        try:
            tags = self.soup.find(id='tableWraper').find_all('td')
            last_update = datetime.strptime(tags[2].text, '%d %b %Y')

            return last_update
        except:
            print(self.label + "error occured")
