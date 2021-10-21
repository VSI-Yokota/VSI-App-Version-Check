# coding: utf-8

import re
from checkers.abstract import AbstractVersionCheck
from datetime import datetime

class CreativeCloudVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Adobe Creative Cloud" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            section_tags = self.soup.find_all(class_='text aem-GridColumn aem-GridColumn--default--12')
            for section_tag in section_tags:
                p_tag = section_tag.find('p')
                date = re.findall('Version.*released on (\d{1,2}/\d{1,2}/\d{4}).*', p_tag.text)
                if len(date) > 0:
                    last_update = datetime.strptime(date[0], '%m/%d/%Y')
                    return last_update
        except Exception as e:
            self.logger.error(self.label + "error occured")
