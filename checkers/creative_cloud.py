# coding: utf-8

from checkers.abstract import AbstractVersionCheck
from datetime import datetime
import re

class CreativeCloudVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Adobe Creative Cloud\t"
        self.url = url

    def get_update_date(self):

        try:
            section_tags = self.soup.find_all(class_='text parbase section')
            for section_tag in section_tags:
                p_tag = section_tag.find('p')
                date = re.findall('Version.*released on (\d{1,2}/\d{1,2}/\d{4}).*', p_tag.text)
                if len(date) > 0:
                    last_update = datetime.strptime(date[0], '%m/%d/%Y')
                    return last_update
        except:
            print(self.label + "error occured")
