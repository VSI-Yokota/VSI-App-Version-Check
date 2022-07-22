# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class WordPressJpSecurityVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "WORDPRESS JP Security" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            date = self.soup.find(id='main').find('article').find(class_='entry-date')
            last_update = datetime.strptime(date.text, '%Y年%m月%d日')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")