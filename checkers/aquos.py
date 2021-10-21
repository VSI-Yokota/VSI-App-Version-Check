# coding: utf-8

import re
from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class AquosVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "AQUOS SH-M08" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            section_tags = self.soup.find_all(class_='section')
            for section_tag in section_tags:
                p_tag = section_tag.find('p')
                date = re.findall('^\d{4}年\d{1,2}月\d{1,2}日', p_tag.text)
                if len(date) > 0:
                    last_update = datetime.strptime(date[0], '%Y年%m月%d日')
                    return last_update

        except Exception as e:
            self.logger.error(self.label + "error occured")
