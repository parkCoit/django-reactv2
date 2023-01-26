import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

OKLAHOMA_MENUS = ["Exit", #0
                "Spec",#1
                "Rename",#2
                "Interval",#3 18세이상만 사용함
                "Norminal",#4
                "Target",#5
                "Partition",#6
                "미완성: Fit",#7
                "미완성: Predicate"]#8
oklahoma_meta = {
    'ACCESS', 'ACR', 'AGEP', 'BATH', 'BDSP', 'BLD', 'CONP', 'COW', 'ELEP',
       'FESRP', 'FKITP', 'FPARC', 'FSCHP', 'FTAXP', 'GASP', 'HHL', 'HHT',
       'HINCP', 'LANX', 'MAR', 'MV', 'NRC', 'R18', 'R65', 'RAC1P', 'RMSP',
       'RWAT', 'SCH', 'SCHL', 'SEX', 'VALP', 'VALP_B1'
}
oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.norminal_variables(),
    "5" : lambda t: t.target()
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''
class Oklahoma:

    def __init__(self):
        self.oklahoma = pd.read_csv('./data/dam/oklahoma/comb32.csv')
        self.my_oklahoma = None

    '''
    1.스펙보기 
    id = SERIALNO  
    이진값 분류 문제
    okhoust - shape(population(19398), columns(230)) dtype('int64') null 값 0 
    '''

    def spec(self):
        pd.set_option('display.max_columns',None) # 전체보기
        pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(self.oklahoma.shape)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)
        print(" --- 3.Info ---")
        print(self.oklahoma.info())
        print(" --- 4.Case Top1 ---")
        print(self.oklahoma.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.oklahoma.tail(3))
        print(" --- 6.Describe ---")
        print(self.oklahoma.describe())
        print(" --- 7.Describe All ---")
        print(self.oklahoma.describe(include='all'))


    def rename_meta(self):
        self.my_oklahoma = self.oklahoma.rename(columns=oklahoma_meta)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)

    '''
    3. 타깃변수(=종속변수 dependent, Y값) 설정
    입력변수(=설명변수, 확률변수,X값)
    -타깃 변수명 : VALP_B1
    -타깃 변수값 : 주택이 중위수 이상이면 1, 아니면 0
    연속형 타깃 변수 회귀 문제
    -타깃 변수명 : VALP
    -타깃 변숫값 : 주택가격
    '''

    def interval_variables(self):
        t = self.oklahoma
        pd.options.display.float_format = '{:.2f}'.format
        cols1 = ['AGEP', 'BDSP','CONP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP']
        print(t[cols1].describe())
        print(t[cols1].skew())
        pd.options.display.float_format = '{:.3f}'.format  # CONP 설문 응답자 월 수선비 지출 x
        print(t['CONP'].value_counts(normalize=True))
        t.drop('CONP', axis=1, inplace=True)  # CONP 월 수선비 제거
        c1 = t['ELEP'] <= 500 # 월 전기료
        c2 = t['GASP'] <= 311 # 월 가스비
        c3 = t['HINCP'] <= 320000 # 가계 소득
        t1 = t[c1 & c2 & c3]
        print(t1.shape)
        cols2 = ['AGEP', 'BDSP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP']  # CONP 제거
        print(t1[cols2].describe())
        print(t1['VALP_B1'].value_counts(normalize=True))
        t1.to_csv('C:/Users/bitcamp/django-react/DjangoServer/blog/save/dam/oklahoma/comb32.csv', index=False)
        print(t1[cols2].corr())  # 구간 변수끼리 상관계수 출력



    def norminal_variables(self):
        ok_home = self.oklahoma
        ok_home['MAR'].value_counts(dropna=False)
        print(pd.crosstab(ok_home['MAR'], columns='count'))
        print(pd.crosstab(ok_home['MAR'], ok_home['VALP_B1']))

        self.oklahoma = ok_home


    def ordinal_variables(self):
        pass

    def target(self):
        df = pd.read_csv('./save/dam/oklahoma/comb32.csv')
        self.data = df.drop(['VALP_B1'], axis=1)
        self.target = df['VALP_B1']
        print(self.data)
        print(self.target)

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Oklahoma()
    while True:
        menu = my_menu(OKLAHOMA_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                oklahoma_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")