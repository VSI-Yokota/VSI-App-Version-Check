# coding: utf-8
from checkers.abstract import AbstractVersionCheck
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


class AdobeSecurityVersionCheck(AbstractVersionCheck):

    def __init__(self, url):
        super().__init__(url)
        self.label = "Adobe Security\t"
        self.url = url

    def get_update_date(self):

        try:
            driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
            driver.implicitly_wait(3)
            driver.get(self.url)

            # iframeへ制御を移動
            iframe = driver.find_element_by_tag_name('iframe')
            driver.switch_to.frame(iframe)

            date_tag = driver.find_element_by_class_name('publish-date')
            date = date_tag.text
            driver.close()
            last_update = datetime.strptime(date, '%b %d, %Y')
            return last_update
        except Exception as e:
            print(e)
            print(self.label + "error occured")


# from checkers.abstract import AbstractVersionCheck
# from datetime import datetime
# import re

# class AdobeSecurityVersionCheck(AbstractVersionCheck):

#     def __init__(self, url):
#         super().__init__(url)
#         self.label = "Adobe Security\t"
#         self.url = url

#     def get_update_date(self):

#         try:
#             date_tags = self.soup.find_all(class_='publish-date-label')
#             # date_tags = self.soup.find_all(class_='publish-date')
#             print(self.soup)
#             print(date_tags)
#             for date_tag in date_tags:
#                 date = re.findall('Last updated on (\d{4}年\d{1,2}月\d{4}日)', date_tag.text)
#                 if len(date) > 0:
#                     last_update = datetime.strptime(date[0], '%m/%d/%Y')
#                     return last_update
#         except:
#             print(self.label + "error occured")
