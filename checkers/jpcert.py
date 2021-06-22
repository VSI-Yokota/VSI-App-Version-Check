# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class JPCertCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "JPCert" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            dt_tag = self.soup.find('table').find_all('td')
            chomp_date = dt_tag[0].text.replace( '\n' , '' )
            last_update = datetime.strptime(chomp_date, '%Y-%m-%d')
            return last_update
        except:
            print(self.label + "error occured")
