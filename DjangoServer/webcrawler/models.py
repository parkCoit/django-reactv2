import urllib

from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from isort._future._dataclasses import dataclass


context = 'C:/Users/bitcamp/django-react/DjangoServer/webcrawler/'


@dataclass
class Scrap:
    html = ""
    parser = ""
    domain = ""
    query_string = ""
    headers = {}
    tag_name = ""
    fname = ""
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.diction, orient='index') #orient='index'는 index를 자동 선언



    def dataframe_to_csv(self, fname):
        path = context+fname
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)