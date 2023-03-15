"""
File     : 06_if_and_loop.py
Title    : 第6章 判斷式與迴圈應用
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

##############################
# 大綱
##############################
# 6.1 判斷式(if elif else)
# 6.2 零數值判斷
# 6.3 迴圈(Loops)
# 6.4 陣列應用 -高維度影像:MNIST 手寫數字辨識資料集

##############################
# 6.1 判斷式(if elif else)
##############################

"""
# case 1
if 布林值:
 	若布林值為 True，執行命令

# case 2
if 布林值:
 	若布林值為 True，執行命令
else:
    若布林值為 False，執行命令

# case 3
if 布林值一:
 	若布林值一為 True，執行命令
elif 布林值二:
 	若布林值二為 True，執行命令
...
else:
 	若布林值一和二...都是 False，執行命令
"""

# elif敘述
a = '+'

if a == '+':
	op = 'PLUS'
elif a == '-':
	op = 'MINUS'
else:
	op = 'UNKNOWN'

op

# 沒有像C語言一樣，有switch的語法
# 布林表示式 – and, or, not
a = 1
b = 6
c = 9

if b >= a and b <= c:
	print('b is between a and c')
    
if not (b < a or c > c):
	print('b is still between a and c')

# if 範例 - 測試所有輸入情形
mynameage = input('輸入姓名與年齡: ')

name = mynameage.split(',')[0]
age = mynameage.split(',')[1]

if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')

# 邏輯錯誤 (Logical Errors)
# if 範例 - age > 200 不會執行
name = 'RWEPA'
age = 300
if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')
elif age > 100:
    print('You are not Alan. 大大')
elif age > 200:
    print('年齡異常')

##############################
# 6.2 零數值判斷
##############################

# 零數值判斷, 以下結果皆為 True
0 == False
0.0 == False
0.000 == False
'' == False

# 非零數值判斷
1 == True     # True
1.23 == True  # False
1.23 == False # False

# 實作練習12
# for + continue 迴圈練習, 篩選出 list 的字串資料
# 提示: 使用 if, for, append, continue 順序非固定
# 結果 ['python', '123.45', 'RWEPA', 'R']
mylist = [1, 3, "python", '123.45', "RWEPA", 100, "R"]

##############################
# 6.3 迴圈(Loops)
##############################

# for 迴圈

# 顯示list元素
for i in [3, 4, 10, 25]:
	print(i)

# 顯示一個字元
for c in "Hello":
	print(c)

# for + range 迴圈
# 顯示 range 元素
for i in range(1, 4):
	print(i)

for i in range(4, -2, -1):
	print(i)
    
# while 迴圈
name = ''
while name != 'Alan Lee':
    print('Please type your name.')
    name = input()
print('Thank you!')

# while + break
while True:
    print('Please type your name.')
    name = input()
    if name == 'Alan Lee':
        break
print('Thank you!')

# while + break + continue
while True:
    print('Who are you?')
    name = input()
    if name != 'Alan':
        continue
    print('Hello, Alan. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

##############################
# 6.4 陣列應用 -高維度影像:MNIST 手寫數字辨識資料集
##############################

# http://yann.lecun.com/exdb/mnist/

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 方法1 回傳 Bunch 資料物件
# 原圖為28*28, 2維展開為1維 28*28=784

mnist_data = fetch_openml("mnist_784") # 網路下載,須一些時間.
xdata = mnist_data["data"] # 70000*784
ydata = mnist_data["target"] # 70000

xdata.ndim  # 2
xdata.shape # (70000, 784)
type(xdata) # pandas.core.frame.DataFrame
xdata.dtypes

# 方法2 直接回傳 X, y

# Load data from https://www.openml.org/d/554
X, y = fetch_openml('mnist_784', return_X_y=True)
# X : 70000*84
# y : 70000

# 以下採用方法2
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=123, 
                                                    test_size=10000)
type(X_train) # DataFrame (早期版本為 numpy.ndarray)

# 將 DataFrame 轉換成 array 物件
X_train = X_train.to_numpy()
y_train = y_train.to_numpy()

type(X_train) # numpy.ndarray
X_train.ndim  # 2
X_train.shape # (60000, 784)
X_train.dtype # dtype('float64')

type(y_train) # numpy.ndarray
y_train.ndim  # 1
y_train.shape # (60000,)
y_train.dtype # dtype('O'), 表示字串

# 繪製數字影像
plt.imshow(X_train[0].reshape(28,28), cmap='binary')

# 實際值
y_train[0] # '5'

# 繪製多個數字影像, 最多一次顯示25個
def plot_images_labels(images, labels, idx, num=10):
    fig = plt.gcf() # 取得目前的 figure
    fig.set_size_inches(12, 14) # 設定圖形大小
    if num > 25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5, 5, 1+i)
        ax.imshow(images[idx].reshape(28,28), cmap='binary')
        title= "Label=" + str(labels[idx])
        ax.set_title(title, fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])        
        idx+=1 
    plt.show()

plot_images_labels(X_train, y_train, 0, 10)
# end
