# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class WordPressSecurityVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "WORDPRESS Security" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date = self.soup.find(class_='widefat').find('tr').find('th')
            last_update = datetime.strptime(date.text, '%B %d, %Y')
            return last_update
        except:
            print(self.label + "error occured")
