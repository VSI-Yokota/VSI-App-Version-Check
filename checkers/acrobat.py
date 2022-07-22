# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class AcrobatVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Acrobat" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            dt_tag = self.soup.find(id='root_content_flex').find('table').find_all('td')
            chomp_date = dt_tag[0].text.replace( '\n' , '' )
            last_update = datetime.strptime(chomp_date, '%b %d, %Y')
            return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
