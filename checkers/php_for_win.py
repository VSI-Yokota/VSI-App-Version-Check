# coding: utf-8

import re
from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class PHP4WindowsVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "PHP FOR WINDOWS" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            main = self.soup.find(id='main-column')
            blocks = main.find_all(class_='block')
            date = []

            for block in blocks:
                innerbox = block.find(class_="innerbox")
                if innerbox:
                    datetext = innerbox.find("h4").text
                    date = re.findall('.*\((.*)\)$', datetext)
                    break

            if len(date) > 0:
                last_update = datetime.strptime(date[0], '%Y-%b-%d %H:%M:%S')
                return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
