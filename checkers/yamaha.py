# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
import re

class YamahaRouterVersionCheckBase(AbstractVersionCheck):

    def get_update_date(self):

        try:
            rows = self.soup.find('table').find_all('tr')
            td_tags = rows[-1].find_all('td')

            for td_tag in td_tags:
                date = re.findall('^\d{4}年\s{0,1}\d{1,2}月\d{1,2}日', td_tag.text)
                if len(date) > 0:
                    last_update = datetime.strptime(date[0], self.date_format)
                    return last_update
        except:
            print(self.label + "error occured")

        
class RTX1200VersionCheck(YamahaRouterVersionCheckBase):

    def __init__(self, url):
        super().__init__(url)
        self.label = "RTX1200\t"
        self.url = url
        self.date_format = '%Y年%m月%d日'


class RTX1210VersionCheck(YamahaRouterVersionCheckBase):

    def __init__(self, url):
        super().__init__(url)
        self.label = "RTX1210\t"
        self.url = url
        self.date_format = '%Y年%m月%d日'

class WXL202VersionCheck(YamahaRouterVersionCheckBase):

    def __init__(self, url):
        super().__init__(url)
        self.label = "WXL202\t"
        self.url = url
        self.date_format = '%Y年 %m月%d日'