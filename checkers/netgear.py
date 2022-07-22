# coding: utf-8

import re
import requests
import time
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class NetgearVersionCheckBase(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.keywords = []

    def get_update_date(self):

        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--log-level=1')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.implicitly_wait(10)
            driver.get(self.url)
            time.sleep(3)

            tbody = driver.find_element_by_id('tbSecurityUpdates')
            tr_list = tbody.find_elements_by_tag_name('tr')

            for tr in tr_list:
                td_list = tr.find_elements_by_tag_name('td')

                if not td_list[0].text.strip():
                    continue

                a = td_list[0].find_element_by_tag_name('a')
                date = datetime.strptime(a.text, '%m/%d/%Y')

                if date < self.target_date:
                    break

                res = requests.get(a.get_attribute('href'))
                res.encoding = res.apparent_encoding
                soup = BeautifulSoup(res.text, features="html.parser")

                for li in soup.find(class_='article-content').find_all('li'):
                    for word in self.keywords:
                        if word in li.text:
                            last_update = date

            driver.close()

            last_update = datetime.strptime(last_update, '%Y/%m/%d')
            return last_update

        except Exception as e:
            self.logger.error(self.label + "error occured")

class ReadyNAS316VersionCheck(NetgearVersionCheckBase):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "ReadyNAS 316" + self.separator
        self.url = url
        self.keywords = ['ReadyNas', 'RN31600']
