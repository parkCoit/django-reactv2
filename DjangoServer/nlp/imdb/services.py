import os
from collections import defaultdict
from math import log, exp

import pandas as pd
from bs4 import BeautifulSoup
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from keras_preprocessing.sequence import pad_sequences
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webcrawler.models import Scrap

class ImdbService:
    def __init__(self):
        global train_input, train_target, test_input, test_target, val_input, val_input, val_target
        # 데이터 셋 불러오기
        (train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
        # 20% 를 검증세트로 떼어놓으면 훈련세트는 80%로 줄어듬
        train_input, val_input, train_target, val_target = train_test_split(
            train_input, train_target, test_size=0.2, random_state=42
        )


    def hook(self):
        self.show_data()
        self.create_model()
        self.preprocess()


    def show_data(self):
        print(train_input.shape, test_input.shape)
        print(len(train_input[0]))
        print(len(train_input[1]))
        print(train_input[0])
        print(train_target[:20])
        lengths = np.array([len(x) for x in train_input])  # 각 리뷰의 길이를 계산해 넘파이 배열에 담기
        print(np.mean(lengths), np.median(lengths))  # mean()함수와 median() 함수를 사용해 리뷰 길이의 평균과 중간값 구하기
        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('frequency')
        plt.show()

    def preprocess(self):
        train_seq = pad_sequences(train_input, maxlen=100) # pad_sequences() 함수를 사용해 train_input의 길이를 100으로 맞춘다

        # print(train_seq.shape)
        # print(train_seq[0])
        # print(train_input[0][-10:])
        # print(train_seq[5])
        val_seq = pad_sequences(val_input, maxlen=100)
        return {'train_seq' : train_seq,
                'val_seq': val_seq,
                'train_target': train_target,
                'val_target': val_target}


    def create_model(self):
        pass

class NaverMovieService(Scrap):
    def __init__(self):
        global url, driver, file_name, encoding, review_train, encoding, review_train, k
        url = f'https://movie.naver.com/movie/point/af/list.naver?&page=1'
        file_name = os.path.join(os.getcwd(), 'nlp/imdb/naver_movie_review_corpus.csv')
        review_train = os.path.join(os.getcwd(), 'nlp/imdb/review_train.csv')
        encoding = "UTF-8"
        self.word_probs = []
        k = 0.5

    def hook(self, new_review):
        # new_review = '안녕하세요 감사합니다'
        self.model_fit()
        result = self.classify(new_review)
        result = f'{round((result * 100))}%'
        return result

    def crawling(self):
        if os.path.isfile(file_name):
            review_csv = pd.read_csv(file_name, header=None, index_col=0)
            ls_review = list(review_csv.index)
            print(ls_review)
        else:
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_td = soup.find_all('td', attrs={"class": "title"})

            reviews = {td.br.next_element.strip(): td.div.em.text
                       for td in all_td
                       if td.br.next_element.strip() != ""}  # strip()함수는 공백 제거(ex) \n)
            df = pd.Series(reviews)
            print(reviews)
            df.to_csv(file_name, header=None)
            driver.close()
            review_csv = pd.read_csv(file_name, header=None, index_col=0)
            ls_review = list(review_csv.index)
            print(ls_review)




    def load_corpus(self):
        corpus = pd.read_table(review_train, sep=',', encoding=encoding)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda: [0,0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts


    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False

    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        # print(word_probs)
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)


    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]

    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)

    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요' : [1,0]
        '별로 재미업어요' : [0,1]
        '''
        num_class0 = len([1 for _, point  in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)

if __name__ == '__main__':
    service = NaverMovieService()
    result = service.hook()
    print(f'긍정률 : {result}')
