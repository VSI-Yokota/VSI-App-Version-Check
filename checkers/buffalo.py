# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class BuffaloVersionCheckBase(AbstractVersionCheck):

    def get_update_date(self):

        try:
            time_tag = self.soup.find('time')
            last_update = datetime.strptime(time_tag.text, '%Y/%m/%d')
            return last_update

        except Exception as e:
            self.logger.error(self.label + "error occured")

class TeraStationVersionCheck(BuffaloVersionCheckBase):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "TeraStation" + self.separator
        self.url = url

class WZR_D1100HVersionCheck(BuffaloVersionCheckBase):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "WZR D1100H" + self.separator
        self.url = url
