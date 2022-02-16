import os
import urllib.request

import requests

from grade import Grade


class Content:
    def __init__(self, __grade: Grade, __year: str, __time: str, __name: str, __url: str):
        self.__grade = __grade
        self.__year = __year
        self.__time = __time
        self.__name = __name
        self.__url = __url

    @property
    def grade(self):
        return self.__grade

    @property
    def year(self):
        return self.__year

    @property
    def time(self):
        return self.__time

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    def download(self, parent_folder_path: str):
        folder_path = parent_folder_path + self.__year + "/" + self.__time + "/"
        file_path = folder_path + self.__name + ".pdf"
        print(folder_path)
        os.makedirs(folder_path, exist_ok=True)
        urllib.request.urlretrieve(self.__url, file_path)
