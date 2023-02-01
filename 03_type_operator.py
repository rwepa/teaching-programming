"""
File     : 03_type_operator.py
Title    : 第3章 資料型別與運算子
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
Encoding : UTF-8
"""

# 大綱
# 3.1 註解
# 3.2 變數
# 3.3 指派多個變數
# 3.4 資料型別
# 3.5 運算子

# 3.1 註解
# 使用一個 #	   用於1行註解
# 使用二個 """  用於超過1行註解或函數之說明文件

# 內縮4個空白鍵之語法
# 區塊語法之最後位置加上冒號(:)

# case1
x = 8
y = 7
if x > y:
    print('x 大於 y')
print("程式設計")

# case2
x = 8
y = 7
if x > y:
    print('x 大於 y')
    print("程式設計")

# case3
x = 7
y = 7
if x > y:
    print('x 大於 y')
    print("程式設計")

# 3.2 變數

# 變數命名
# 1.必須以字母或下底線字符開頭
# 2.不能以數字開頭
# 3.只能包含字母、數字和下底線（A-z、0-9 和 _ ）
# 4.區分大小寫
# 5.雙下底線開頭與結尾的名稱已經由 Python 保留, 例: __init__
# 例: customer、Customer 和 CUSTOMER 是不同的變數

# 合法變數
大數據 = 1 # 中文亦可,建議不要使用
CustomerSaleReport = 1
_CustomerSaleReport = 1
Customer_Sale_Report = 1
customer_sale_report = 1

# 變數可以重新指派改變其值
CustomerSaleReport = 123

# 不合法變數
$CustomerSaleReport = 1 # SyntaxError: invalid syntax
2020_sale = 100 # SyntaxError: invalid decimal literal
break = 123 # SyntaxError: invalid syntax

# 內建保留字
dir(__builtins__)
len(dir(__builtins__)) # 160

# 3.3 指派多個變數
address1 = "台北", "台中", "高雄"
type(address1) # tuple
x, y, z = address1
print(x)
print(y)
print(z)
type(x) # str

address2 = ["台北", "台中", "高雄"]
type(address2) # list
x, y, z = address2
print(x)
print(y)
print(z)
type(x) # str

# Python 程式撰寫規則 (Python Style Rules)
# https://google.github.io/styleguide/pyguide.html

# 3.4 資料型別
# 資料型別(資料型態)
# https://docs.python.org/3/library/stdtypes.html

# 廣義 Data Types
# Text Type:      str
# Numeric Types:  int, float, complex
# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview
# Sequence Types: list, tuple, range
# Set Types:	  set, frozenset
# Mapping Type:	  dict
# 參考: https://www.w3schools.com/python/

# 資料型別-範例

# 整數 int
x1 = 1
type(x1)

# 浮點數 float
x2 = 1.234
type(x2)

# 複數  complex, R: 使用 1+2i
x3 = 1+2j
type(x3)

# 布林值 (Boolean)
x4 = True
type(x4)
x4 + 10

# None值
import numpy as np
None == False
None == 0
False == 0
True == 1
None == np.nan
None == None

# 整數亂數
import random
random.seed(168) # 設定亂數種子, 每次 myrandom 結果, 皆是相同為96
myrandom = random.randrange(1, 100) # 結果為 1,2,...99 整數, 不包括100
myrandom

# 3.5 運算子

# 運算子
3 + 5
3 + (5 * 4)
3 ** 2
"Hello" + "World"
1 + 1.234
7 / 2
7 // 2
7 % 2
2 ** 10
1.234e3 - 1000

x5 = 1 == 2
x5
x5 + 10

# 位移運算子: << 向左位移
# 位移運算子: >> 向右位移
a = 4 << 3 # 0100 --> 0100000, 32 16 8 4 2 1
print(a)

b = a * 4.5
print(b)

c = (a+b)/2.5

# 指派運算子
x = 9
x+=2
print(x)

# end
