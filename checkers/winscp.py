# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class WinSCPVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "WinSCP" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            version = self.soup.find(class_='items-list-blocks-item-heading').text
            date = self.soup.find(class_='items-list-blocks-item-date').text
            last_update = datetime.strptime(date, 'Published:%Y-%m-%d')

            # 開発版リリースは無視
            if 'RC' in version:
                self.ignore = True

            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
