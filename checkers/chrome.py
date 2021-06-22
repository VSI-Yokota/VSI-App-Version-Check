# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class ChromeVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Chrome" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date = self.soup.find(id='Blog1').find(class_='post-header').find(class_='publishdate')
            chomp_date = date.text.replace( '\n' , '' )
            last_update = datetime.strptime(chomp_date, '%A, %B %d, %Y')
            return last_update
        except:
            print(self.label + "error occured")
