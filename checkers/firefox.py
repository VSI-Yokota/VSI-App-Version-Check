# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class FirefoxVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Firefox" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            # transfar to detail page
            latest_release_list = self.soup.find(class_='c-release-list').find('li')
            miner_versions = latest_release_list.find('ol')

            if (miner_versions is None):
                latest_version_link = latest_release_list.find('a')
            else:
                miner_tags = miner_versions.find_all('a')
                latest_version_link = miner_tags[-1]

            detail = FirefoxVersionDetailCheck( self.url + latest_version_link['href'])
            return detail.get_update_date()
        except Exception as e:
            self.logger.error(self.label + "error occured")

class FirefoxVersionDetailCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Firefox detail\t"

    def get_update_date(self):
        try:
            date = self.soup.find(class_='c-release-date')
            last_update = datetime.strptime(date.text, '%B %d, %Y')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
