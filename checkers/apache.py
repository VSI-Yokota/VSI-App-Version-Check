# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class ApacheVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Apache" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            content_titles = self.soup.find(id='apcontents').find_all("h1")
            for title in content_titles:
                date = title.find("span")

                if date is not None:
                    last_update = datetime.strptime(date.text, '%Y-%m-%d')
                    return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")



