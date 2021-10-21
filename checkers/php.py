# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class PHPVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "PHP" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            news = self.soup.find(class_='newsentry')
            time = news.find('time')
            last_update = datetime.strptime(time.text, '%d %b %Y')
            return last_update
        except Exception as e:
            self.logger.error("PHP\terror occured")



