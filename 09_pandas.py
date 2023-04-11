"""
File     : 09_pandas.py
Title    : 第9章 pandas模組
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

##############################
# 大綱
##############################

# 9.1 pandas 簡介
# 9.2 pandas 序列(Series)物件
# 9.3 pandas 資料框(DataFrame)物件 
# 9.4 匯入 CSV 檔案
# 9.5 匯入 Excel 檔案
# 9.6 匯入 SAS 檔案
# 9.7 資料匯出

##############################
# 9.1 pandas 簡介
##############################

# https://pandas.pydata.org/
# pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

# pandas documentation:
# https://pandas.pydata.org/docs/

# pandas API reference
# https://pandas.pydata.org/docs/reference/index.html

# 10 minutes to pandas
# https://pandas.pydata.org/docs/user_guide/10min.html

# 載入2大套件 numpy, pandas
import numpy as np  # Python Scientific Computing Library
import pandas as pd # Python Data Analysis Library

##############################
# 9.2 pandas 序列(Series)物件
##############################

# s = pd.Series(data, index=index)
# data 包括使用 array, Iterable, dict, scalar value
# 序列包括指標(Index) 與值(Value), 指標採用預設整數型態指標 0,1,2,...

# (1).Series - 使用 ndarray
s = pd.Series(data = np.random.randn(5), index=["a", "b", "c", "d", "e"])
s
# a   -0.492604
# b   -0.073386
# c   -0.063632
# d    0.197128
# e    0.178333
# dtype: float64
type(s) # pandas.core.series.Series

# (2).Series -使用 Iterable - 序列(tuple)
s1 = pd.Series((1,3,5,np.nan,6,8))
s1

# (3).Series - 使用 Iterable - 串列(List)
s2 = pd.Series([1,3,5,np.nan,6,8])
s2

s1 == s2 # equality 相等, 比較每個元素是否相同, 大部分使用此功能.
s1 is s2 # identity 相同, 比較二物件是否指向同一個記憶體

id(s1)
id(s2) # 與id(s1) 不相等

# "==" 與 "is" ("is not") 應用

# identity - 使用 id 函數, 查看說明 help(id). 相同程式 id 結果,每次不一定相同.
# https://realpython.com/python-is-identity-vs-equality/

a = 'Hello world'
b = 'Hello world'
a == b
a is b
id(a)
id(b)

# 整數 [-5 ~ 256] 會使用相同記憶體位址功能
a = 256
b = 256
a == b   # True
a is b   # True
id(a)
id(b)

a = 1000
b = 1000
a == b   # True
a is b   # False
id(a)
id(b)

x1 = np.nan
x2 = np.nan
id(x1)
id(x2) # 與上面結果相同
x1 == x2 # False
x1 is x2 # True

# (4).Series - 使用 Iterable - 字典(Dict)
# 在 pandas 模組之中, NaN 表示為 "not a number"
x = {"x1": 1, "x2": 2, "a": np.nan, "b": 3, "c": 4}
c = pd.Series(x)
c

# (5).Series - 使用 scalar value
pd.Series(999.0, index=["a", "b", "c", "d", "e"])

##############################
# Series 使用 ndarray-like 操作
##############################
c
# x1    1.0
# x2    2.0
# a     NaN
# b     3.0
# c     4.0
# dtype: float64

c[0]              # 1.0
c[1]              # 2.0
c[-1]             # 4.0
c[:3]
# x1    1.0
# x2    2.0
# a     NaN
# dtype: float64

c[c > c.median()]
c[[1, 3, 2]]
np.exp(c)
c.dtype

# Series.array 是 pandasExtensionArray.
# ExtensionArray 是包括一個或多個 numpy.ndarray 的 thin wrapper類別
c.array      # 將 series 轉換為 PandasArray

c1 = c.to_numpy() # 將 series 轉換為 NumPy ndarray
c1

c2 = c.to_numpy
c2

c1 == c2
c1 is c2

##############################
# Series 使用 dict-like 操作
##############################
c

c['x1']
c['a'] = np.pi

'x1' in c

c.get("a")
c.get("e") # None

##############################
# 9.3 pandas 資料框(DataFrame)物件
##############################

# 方法1.建立指標與值,再合併為資料框

# 步驟1-建立 DatetimeIndex 物件
dates = pd.date_range('20210801', periods=6) # 日期指標
dates
type(dates)

# 步驟2-建立 DataFrame
# 欄位名稱: A, B, C, D
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1
type(df1)

# 方法2.使用字典建立資料框
df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20210801'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
df2

# dtypes: 顯示各欄位的資料型態
df2.dtypes

# 方法3.使用 list of dicts 建立資料框

# 預設指標
mydata = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
df3 = pd.DataFrame(mydata)
df3

# 客製化指標
df4 = pd.DataFrame(mydata, index=["first", "second"])
df4

# 方法4.使用 dict of tuples 建立資料框
# 使用 tuples dictionary, 可建立 MultiIndexed dataframe(階層式指標資料框)
df5 = pd.DataFrame(
    {
        ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
        ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
        ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
        ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
        ("b", "b"): {("A", "D"): 10, ("A", "B"): 11},
    }
)
df5
type(df5)

# 方法5.使用 list of dataclasses 建立資料框
# pandas 1.1.0 新增功能, 參考 PEP 557 -- Data Classes
# list of dataclasses 類似於 list of dictionaries
# https://www.python.org/dev/peps/pep-0557/

from dataclasses import make_dataclass
Mydata = make_dataclass("Stations", [("x", int), ("y", int)])
Mydata
df6 = pd.DataFrame([Mydata(0, 0), Mydata(0, 3), Mydata(2, 3), Mydata(1, 2)])
df6

##############################
# 資料檢視
##############################
np.random.seed(123)
dates = pd.date_range('20210801', periods=6) # 日期指標
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1

# head 顯示前 5 筆資料, 此功能與 R 顯示 6 筆不相同.
df1.head()

df1.head(3) # 顯示前 3 筆資料

df1.tail()  # 顯示後 5 筆資料

# 顯示指標(index)
df1.index

# 欄名稱(columns)
df1.columns

# 資料值(values)
df1.values

# T 資料轉置, 類似將原本長資料 (Long data), 轉換為寬資料 (Wide data)
df1.T

##############################
# describe 統計摘要(statistic summary)
##############################

# count 個數
# mean 平均值
# std  標準差 standard deviation, 一般希望愈小愈好
# min  最小值
# 25%  25百分位數
# 50%  50百分位數, 中位數 median
# 75%  75百分位數 (quantile)
# max  最大值

df1.describe()

##############################
# 排序
##############################

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# (1).排序 sort_index

# axis為排序的軸，0表示 rows index(列指標)，1表示 columns index(行指標)
# 當對資料"列" 進行排序時，axis必須設置為0.
# df.sort(["A"]) 新版不支援 sort 函數, 改用 sort_values 或 sort_index

# ascending =FALSE, 即遞增是FALSE, 表示遞減是TRUE, 結果為D,C,B,A
df1.sort_index(axis=1, ascending=False)

# (2).排序 sort_values

# 依照 B 欄大小, 由小至大排序 (預設值是遞增)
df1.sort_values(by='B')

# 依照 B 欄大小, 改為由大至小排序 (遞減)
df1.sort_values(by='B', ascending = False)

# 依照 B 欄大小, 將 nan 排在最前面或最後面
df1.iloc[2, 0] = np.nan
df1
df1.sort_values(by='A')
df1.sort_values(by='A', na_position = 'first')

# 實作練習
# 使用 mydf 進行A欄位遞增, B欄位遞減排序
#    A   B   C
# 0  1  10  aa
# 1  2  24  bb
# 2  2  26  cc
# 3  4   9  dd
# 4  2  29  aa

# analysis:
mydf = pd.DataFrame(
    {'A': [1,2,2,4,2],
     'B': [10,24,26,9,29],
     'C': ['aa', 'bb', 'cc', 'dd', 'aa']})
mydf

mydf.sort_values(by=['A', 'B'], ascending = [True, False])

mydf.sort_values(by=['A', 'B'], ascending = [True, False],  inplace=True) # 更改 mydf 內容

##############################
# 資料列,行選取
##############################
import numpy as np
import pandas as pd
np.random.seed(123)
dates = pd.date_range('20210801', periods=6) # 日期指標
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1

# 選取行
df1['A']
df1.A
df1[['A', 'B']]

# 選取列, df[1:4]選取第1至第3列(4-1=3), 此功能與 R 不同.
df1
df1[1:4]

# 使用 loc
df1.loc[:, ['A','B']]

# 使用 iloc
df1.iloc[2] # 指標為第2列

df1.iloc[2:4,]
df1.iloc[2:4, :]

df1.iloc[, 2]    # ERROR
df1.iloc[:, 2]   # OK
df1.iloc[:, 2:4] # OK

# Boolean Indexing 邏輯值(條件式)資料選取
df1.loc[dates[2]]
df1.loc['20210803']

df1.loc['20210803', ['A', 'B']]
df1.loc['20210802':'20210804', ['A', 'B']]

df1.iloc[[1,2,4],[0,2]] # 選取不連續範圍

df1.iloc[2,2]
df1.iat[2,2]

df1[df1 > 1.5]
df1[df1.A > 1.5]

# 使用 .isin - 範例1
df1[df1.index.isin(['2021-08-02', '2021-08-04'])]

# 使用 .isin - 範例2

df2 = df1.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]

# Missing Data 遺漏值 np.NaN (np.nan), R: 使用NA
df3 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df3.loc[dates[0]:dates[1],'E'] = 1
df3

# 判斷何者為NaN
pd.isnull(df3)

# 刪除列中包括 NaN
df3.dropna(how='any')

# 將遺漏值填入值
df3.fillna(value=999)

##############################
# 列,行的匯總計算
##############################
"""
A B C
1 5 
2 NaN 10
3 7 11
4 8 12
"""
df = pd.read_clipboard()
df
df.dtypes
df.isnull()

# 計算每行平均
df.mean()

# 計算每列平均
df.mean(1)

# apply 將資料套用至函數
df.apply(np.cumsum) # 各資料行累計加總

##############################
# 列合併 append, concat 
##############################

np.random.seed(123)
df = pd.DataFrame(np.random.randn(3, 4))
df

pieces = pd.DataFrame(np.random.randn(2, 4))
pieces

# append 列合併
df.append(pieces, ignore_index=True)

# concat 列合併, 類似 R的 rbind
pieces1 = pd.DataFrame(np.random.randn(2, 4))
pieces1

pd.concat([df, pieces, pieces1], ignore_index=True)

##############################
# Grouping 群組計算
##############################
# https://github.com/rwepa/DataDemo/blob/master/Cars93.csv

import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df = df[['Manufacturer', 'Price', 'AirBags', 'Horsepower', 'Origin']]

df.head()

df_AirBags = df.groupby('AirBags')
type(df_AirBags)

print(df_AirBags.groups)

# 群組 - 2個維度
df_AirBagsOrigin = df.groupby(['AirBags', 'Origin'])

# 群組大小
df_AirBagsOrigin.size()

# 篩選群組
df_AirBags.get_group('Driver & Passenger')

# 群組總和
df_AirBags.sum()

# 群組平均
df_AirBags.mean()

# agg - 每行計算min
df_AirBags.agg('min')

# agg - 每行計算max
df_AirBags.agg('max')

# 資料摘要
import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df.dtypes # object: 字串, float64: 含小數點數值

df.describe() # 無法顯示所有欄位
df.describe(include='all') # 顯示所有欄位

# 顯示所有資料
pd.set_option('display.max_rows', None, 'display.max_columns', None) # None 沒有限制
df.describe()
df

##############################
# 9.4 匯入 CSV 檔案
##############################

# pandas IO 模組
# https://pandas.pydata.org/docs/user_guide/io.html

import pandas as pd
print(pd.__version__) # 1.4.4

# 下載 marketing.csv 至 C:\pythondata\data 資料夾
# https://github.com/rwepa/DataDemo/blob/master/marketing.csv

# 匯入資料
marketing = pd.read_csv('C:/mydata/marketing.csv')
marketing # 200*4

# 資料摘要
marketing.describe()

# 有NaN
marketing.isnull().sum()

marketing['facebook']

# 將 facebook 變數的 NaN資料, 以中位數填滿
marketing['facebook'].fillna(marketing['facebook'].median, inplace = True)

# 沒有NaN
marketing.isnull().sum()

print(marketing)
# RecursionError: maximum recursion depth exceeded

##############################
# 9.5 匯入 Excel 檔案
##############################

# 匯入 Excel 檔案, 全國訂單明細.xlsx
# https://github.com/rwepa/DataDemo/blob/master/全國訂單明細.xlsx

sales = pd.read_excel(io = 'C:/mydata/全國訂單明細.xlsx', sheet_name = '全國訂單明細')
sales # 8568*19
sales.head()

##############################
# 9.6 匯入 SAS 檔案
##############################

# 匯入 SAS 檔案, h_nhi_ipdte103.sas7bdat
# 資料說明: 103年模擬全民健保處方及治療明細檔_西醫住院檔
# 資料筆數: 14297
# 欄位個數: 80
# 檔案大小: 7.25MB
# https://github.com/rwepa/DataDemo/blob/master/h_nhi_ipdte103.sas7bdat

ipdate = pd.read_sas(filepath_or_buffer = 'C:/mydata/h_nhi_ipdte103.sas7bdat')
ipdate # 14297*80
ipdate.head()

##############################
# 9.7 資料匯出
##############################
df = pd.DataFrame({'姓名': ['ALAN', 'LEE'],
                   '地址': ['台北市', '新北市'],
                   '年資': [10, 20]})
df
#      姓名   地址  年資
# 0  ALAN  台北市  10
# 1   LEE  新北市  20

df.to_csv('data/df.csv', index = False) # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf-8') # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf_8_sig') # OK
# end
