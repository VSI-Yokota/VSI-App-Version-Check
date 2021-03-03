# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
import re

class PHP4WindowsVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "PHP FOR WINDOWS\t"
        self.url = url

    def get_update_date(self):

        try:
            main = self.soup.find(id='main-column')
            text = main.find(class_='block').find(class_="innerbox").find("h4").text
            date = re.findall('.*\((.*)\)$', text)

            if len(date) > 0:
                last_update = datetime.strptime(date[0], '%Y-%b-%d %H:%M:%S')
                return last_update
        except:
            print(self.label + "error occured")

        

