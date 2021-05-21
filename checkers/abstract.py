# coding: utf-8

from abc import ABC
from abc import abstractmethod
from bs4 import BeautifulSoup
import requests

'''
バージョンチェック抽象クラス
'''
class AbstractVersionCheck(ABC):

    def __init__(self, url, delay=0):
        self.label = ''
        self.url = ''
        try:
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            self.soup = BeautifulSoup(res.text, features="html.parser")
        except :
            print(self.__class__.__name__ + " html parse error")

        
    @abstractmethod
    def get_update_date(self):
        pass

   
    def check(self, target_date):

        if not hasattr(self, 'soup'):
            print(self.label + "soup was not found")
            return

        last_update = self.get_update_date() 
        if last_update is None:
            print(self.label + " last update couldn't retrieve from this site. please check on yourself." + "\turl :" + self.url)
        elif target_date <= last_update:
            print(self.label + " may have been changed version. latest article date was " + last_update.strftime('%Y/%m/%d') + "\turl :" + self.url)
        else :
            print(self.label + "none. latest article date was " + last_update.strftime('%Y/%m/%d'))
