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

def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    print(titles)
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    print(diction)
    arg.dict_to_dataframe()
    arg.dataframe_to_csv("result.csv")  # csv파일로 저장


def MelonMusic(arg):
    req = urllib.request.Request(arg.domain, headers=arg.headers)
    soup = BeautifulSoup(urlopen(req), arg.parser)
    _ = 0
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}")  # 디버깅
     for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
    diction = {}
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv("results.csv")

def riot(arg):
    req = urllib.request.Request(arg.domain+arg.query_string, headers=arg.headers)
    soup = BeautifulSoup(urlopen(req), arg.parser)
    #soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    title = {"class": arg.class_names}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a')['href'] for i in titles if i.find('a') is not None ]
    print(titles)



class ScrapController(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def menu_1():
        scrap = Scrap()
        scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
        scrap.query_string = "20221101"
        scrap.parser = "lxml"
        scrap.class_names = ["title", "artist"]
        scrap.tag_name = "p"
        BugsMusic(scrap)



    @staticmethod
    def menu_2():
        scrap = Scrap()
        scrap.headers = {'User-Agent': "Mozilla/5.0"}
        scrap.domain = "https://www.melon.com/chart/index.htm"
        scrap.parser = "lxml"
        scrap.class_names = ["title", "artist"]
        scrap.tag_name = "div"
        MelonMusic(scrap)

    @staticmethod
    def menu_3():
        scrap = Scrap()
        scrap.headers = {'User-Agent': "Mozilla/5.0"}
        scrap.domain = 'https://fow.kr/find/'
        scrap.query_string = 'hideonbush'
        scrap.parser = "lxml"
        scrap.class_names = "recent_td"
        scrap.tag_name = "td"
        riot(scrap)


music_menus = ["Exit",  # 0
               "벅스뮤직",
               "멜론뮤직",
               "포우"]  # 8

music_menu = {
    "1": lambda t: t.menu_1(),
    "2": lambda t: t.menu_2(),
    "3": lambda t: t.menu_3()

}

if __name__ == '__main__':



    t = ScrapController()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(music_menus)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                music_menu[menu](t)

            except KeyError:
                print(" ### Error ### ")