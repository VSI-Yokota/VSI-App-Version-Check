# coding: utf-8

import requests
from abc import ABC
from abc import abstractmethod
from bs4 import BeautifulSoup
from logging import getLogger

'''
バージョンチェック抽象クラス
'''
class AbstractVersionCheck(ABC):

    def __init__(self, target_date, url, delay=0):
        self.logger = getLogger(__name__)
        self.target_date = target_date
        self.label = ''
        self.url = ''
        self.separator = ','
        self.ignore = False
        try:
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            self.soup = BeautifulSoup(res.text, features="html.parser")
        except Exception as e:
            self.logger.error(self.__class__.__name__ + " html parse error")


    @abstractmethod
    def get_update_date(self):
        pass


    def check(self, target_date):
        try:
            ret = ''
            if not hasattr(self, 'soup'):
                return (self.label + "soup was not found\n")

            last_update = self.get_update_date()

            if last_update is None or target_date is None:
                return self.label + " last update couldn't retrieve from this site. please check on yourself." + self.separator + self.separator + self.url + "\n"
            elif self.ignore:
                return self.label + " update is not applicable. latest article date was" + self.separator + last_update.strftime('%Y/%m/%d') + "\n"
            elif target_date <= last_update:
                return self.label + " may have been changed version. latest article date was" +  self.separator + last_update.strftime('%Y/%m/%d') + self.separator + self.url + "\n"
            else :
                return self.label + "none. latest article date was" + self.separator + last_update.strftime('%Y/%m/%d') + "\n"
        except Exception as e:
            self.logger.error(e)

    def delete_blank_line(s):
        return ''.join(filter(lambda x: x.strip(), s.split('\n')))