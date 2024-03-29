# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class OpenSSLVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Open SSL\t"
        self.url = url

    def get_update_date(self):

        try:
            table = self.soup.find(class_='newsflash')
            date_cols = table.find_all(class_="d")

            for date_tag in date_cols:
                date = date_tag.text
                if len(date) > 0 and date != "Date":
                    last_update = datetime.strptime(date, '%d-%b-%Y')
                    return last_update
        except:
            print(self.label + "error occured")

        

