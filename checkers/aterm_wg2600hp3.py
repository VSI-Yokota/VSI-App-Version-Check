# coding: utf-8

import re
from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class AtermWG2600HP3VersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Aterm WG2600HP3" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            td_tags = self.soup.find(id='soft_fw').find_all('td')

            for td_tag in td_tags:
                date = re.findall('^\d{4}/\d{1,2}/\d{1,2}$', td_tag.text)
                if len(date) > 0:
                    last_update = datetime.strptime(date[0], '%Y/%m/%d')
                    return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
