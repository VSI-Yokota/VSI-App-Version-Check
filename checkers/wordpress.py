# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class WordPressVersionCheckBase(AbstractVersionCheck):

    def get_update_date(self):

        try:
            rows = self.soup.select_one('.releases.latest').find_all('td')

            for row in rows:
                date = row.text
                try:
                    last_update = datetime.strptime(date, self.date_format)
                    break
                except Exception as e:
                    pass

            return last_update
        except Exception as e:
            self.logger.error(e)


class WordPressVersionCheck(WordPressVersionCheckBase):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "WORDPRESS" + self.separator
        self.date_format = "%B %d, %Y"
        self.url = url


class WordPressJPVersionCheck(WordPressVersionCheckBase):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "WORDPRESS JP" + self.separator
        self.date_format = u"%Y年%m月%d日"
        self.url = url