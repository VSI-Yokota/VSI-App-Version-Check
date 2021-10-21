# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class IOSVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "IOS" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            tags = self.soup.find(id='tableWraper').find_all('td')
            last_update = datetime.strptime(tags[2].text, '%d %b %Y')

            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
