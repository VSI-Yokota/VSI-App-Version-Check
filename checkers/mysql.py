# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
import re

class MySQLVersionCheck(AbstractVersionCheck):

    def get_update_date(self):

        try:
            sections = self.soup.find(class_='toc').find_all(class_='section')
            for section in sections:

                date = re.findall('.*\((\d{4}-\d{2}-\d{2}), General Availability\).*', section.text)

                if len(date) > 0:
                    last_update = datetime.strptime(date[0], '%Y-%m-%d')
                    return last_update
        except:
            print(self.label + "error occured")

        
class MySQL56VersionCheck(MySQLVersionCheck):
    def __init__(self, url):
        super().__init__(url)
        self.label = "MySQL5.6" + self.separator
        self.url = url


class MySQL57VersionCheck(MySQLVersionCheck):
    def __init__(self, url):
        super().__init__(url)
        self.label = "MySQL5.7" + self.separator
        self.url = url

class MySQL80VersionCheck(MySQLVersionCheck):
    def __init__(self, url):
        super().__init__(url)
        self.label = "MySQL8.0" + self.separator
        self.url = url
