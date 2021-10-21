# coding: utf-8

import time
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AdobeSecurityVersionCheck(AbstractVersionCheck):

    def __init__(self, target_date, url):
        super().__init__(target_date, url)
        self.label = "Adobe Security" + self.separator
        self.url = url

    def get_update_date(self):

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(10)
            driver.get(self.url)
            time.sleep(5)

            # iframeへ制御を移動
            iframe = driver.find_element_by_tag_name('iframe')
            driver.switch_to.frame(iframe)

            date_tag = driver.find_element_by_class_name('publish-date')
            date = date_tag.text
            driver.close()
            last_update = datetime.strptime(date, '%b %d, %Y')
            return last_update
        except Exception as e:
            self.logger.error(e)
            self.logger.error(self.label + "error occured")


# from checkers.abstract import AbstractVersionCheck
# from datetime import datetime
# import re

# class AdobeSecurityVersionCheck(AbstractVersionCheck):

#     def __init__(self, target_date, url):
#         super().__init__(target_date, url)
#         self.label = "Adobe Security\t"
#         self.url = url

#     def get_update_date(self):

#         try:
#             date_tags = self.soup.find_all(class_='publish-date-label')
#             # date_tags = self.soup.find_all(class_='publish-date')
#             self.logger.error(self.soup)
#             self.logger.error(date_tags)
#             for date_tag in date_tags:
#                 date = re.findall('Last updated on (\d{4}年\d{1,2}月\d{4}日)', date_tag.text)
#                 if len(date) > 0:
#                     last_update = datetime.strptime(date[0], '%m/%d/%Y')
#                     return last_update
#         except Exception as e:
#             self.logger.error(self.label + "error occured")
