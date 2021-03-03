# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
import re

class BuffaloVersionCheckBase(AbstractVersionCheck):

    def get_update_date(self):

        try:
            time_tag = self.soup.find('time')
            last_update = datetime.strptime(time_tag.text, '%Y/%m/%d')
            return last_update

        except:
            print(self.label + "error occured")

class TeraStationVersionCheck(BuffaloVersionCheckBase):

    def __init__(self, url):
        super().__init__(url)
        self.label = "TeraStation\t"
        self.url = url

class WZR_D1100HVersionCheck(BuffaloVersionCheckBase):

    def __init__(self, url):
        super().__init__(url)
        self.label = "WZR D1100H\t"
        self.url = url
