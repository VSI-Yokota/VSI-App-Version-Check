# coding: utf-8

import re
from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class KeePassVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "KeePass" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            pattern = 'n\d+'
            href = self.soup.find(href=re.compile(pattern)).get('href')
            match = re.search('\d+', href)
            last_update = datetime.strptime(match.group(), '%y%m%d')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
