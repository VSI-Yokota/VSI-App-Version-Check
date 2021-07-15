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
        self.separator = ','
        self.chrome_driver = '/Applications/chromedriver'
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

        ret = ''
        if not hasattr(self, 'soup'):
            return (self.label + "soup was not found\n")

        last_update = self.get_update_date() 

        if last_update is None or target_date is None:
            return self.label + " last update couldn't retrieve from this site. please check on yourself." + self.separator + self.separator + self.url + "\n"
        elif target_date <= last_update:
            return self.label + " may have been changed version. latest article date was" +  self.separator + last_update.strftime('%Y/%m/%d') + self.separator + self.url + "\n"
        else :
            return self.label + "none. latest article date was" + self.separator + last_update.strftime('%Y/%m/%d') + "\n"
