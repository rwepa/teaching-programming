"""
File     : 05_numpy_and_reshape.py
Title    : 第5章 使用NumPy模組與reshape應用
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

##############################
# 大綱
##############################
# 5.1 Numpy模組簡介
# 5.2 一維陣列
# 5.3 二維陣列
# 5.4 陣列儲存與載入
# 5.5 常數 Constants
# 5.6 亂數
# 5.7 陣列的屬性
# 5.8 一維陣列 - loop 處理
# 5.9 二維陣列 - loop 處理
# 5.10 陣列運算
# 5.11 reshape 應用
# 5.12 建立副本
# 5.13 向量化處理

##############################
# 5.1 Numpy模組簡介
##############################

# https://numpy.org/

# Numpy 6大功能
# 1.POWERFUL N-DIMENSIONAL ARRAYS: 
# + Fast and versatile(快速, 多功能)
# + the NumPy vectorization(向量化)
# + indexing(指標化) 
# + broadcasting concepts(廣播概念)

# 2.NUMERICAL COMPUTING TOOLS: 
# NumPy offers comprehensive mathematical functions, random number generators, 
# linear algebra routines, Fourier transforms, and more.

# 3.OPEN SOURCE: Distributed under a liberal BSD license, NumPy is developed 
# and maintained publicly on GitHub by a vibrant, responsive, and diverse community.

# 4.INTEROPERABLE: NumPy supports a wide range of hardware and computing platforms, 
# and plays well with distributed, GPU, and sparse array libraries.

# 5.PERFORMANT: The core of NumPy is well-optimized C code. Enjoy the flexibility 
# of Python with the speed of compiled code.

# 6.EASY TO USE: NumPy’s high level syntax makes it accessible and productive 
# for programmers from any background or experience level.


# Numpy 安裝
# conda install numpy
# pip install numpy

import numpy as np

# numpy 模組使用 numpy.ndarray 物件不可使用混合資料型態, 例: 數值+字串混合會有錯誤.
##############################
# 5.2 一維陣列
##############################

# 使用 tuple 或 list 建立一維陣列
a = np.array([1, 2, 3, 4, 5])
b = np.array((3, 9, 1, 10, 5), dtype=float) 

print(a)
print(b)

print(type(a)) # numpy.ndarray
print(type(b))

print(a[0], a[1], a[2], a[3])

b[0] = 5    
print(b) 

b[4] = 0
print(b)

# 排序
np.sort(b)

##############################
# 5.3 二維陣列
##############################

# 使用巢狀清單建立二維陣列
# axis 0:列, axis 1:行
a = np.array([[1,2,3],[4,5,6]])
a 

print(type(a))

print(a[0, 0], a[0, 1], a[0, 2])

print(a[1, 0], a[1, 1], a[1, 2])

a[0, 0] = 6
a[1, 2] = 1
print(a)

# np.arrange
a = np.arange(5) # [0 1 2 3 4]
print(a) 

b = np.arange(1, 11, 2) # 1<= x < 11
print(b) # [1 3 5 7 9]

# np.zeros
np.zeros(5) # array([0., 0., 0., 0., 0.])

np.zeros(5, dtype=int) # array([0, 0, 0, 0, 0])

np.zeros((3, 2)) # 建立3列,2行皆為零的陣列
# array([[0., 0.],
#        [0., 0.],
#        [0., 0.]])

# np.ones 
np.ones(3) # array([1., 1., 1.])

# 設定 dtype
np.ones(3, dtype=np.int64)

# np.full
np.full(shape = (3, 4), fill_value = 99)
# array([[99, 99, 99, 99],
#        [99, 99, 99, 99],
#        [99, 99, 99, 99]])

# zeros_like
a = np.array([[1,2,3], [4,5,6]])
a
# array([[1, 2, 3],
#        [4, 5, 6]])

np.zeros_like(a)
# [[0 0 0]
#  [0 0 0]]

# ones_like
np.ones_like(a)
# [[1 1 1]
#  [1 1 1]]

##############################
# 5.4 陣列儲存與載入
##############################

# 實作練習
# 使用 save 將 Numpy 陣列 a 儲存成外部檔案
outputfile = 'myarray.npy'
with open(outputfile, 'wb') as fp:
    np.save(fp, a)

# 使用 load 將外部檔案匯入至Numpy陣列
import numpy as np
outputfile = "myarray.npy"
with open(outputfile, 'rb') as fp:
    mydata = np.load(fp)
print(mydata)

##############################
# 5.5 常數 Constants
##############################

import numpy as np

np.Inf # 無限大 inf

np.NAN # nan

# 新版本使用 nan
np.nan

np.pi # 3.141592653589793

# Euler’s constant, base of natural logarithms
# Napier’s constant(蘇格蘭數學家約翰·納皮爾)
np.e # 2.718281828459045

# 三角函數
# sin(30度) = sin(pi/6) = 0.5
# sin(45度) = sqrt(2)/2 = 0.707
# sin(60度) = sqrt(3)/2 = 0.866
# sin(90度) = 1
a = np.array([30, 45, 60, 90])
np.sin(a*np.pi/180)

##############################
# 5.6 亂數
##############################

import numpy as np

np.random.seed(123) # 設定亂數種子, 須輸入 >= 1 的整數

# random 產生0.0~1.0之間的1個亂數
x1 = np.random.random()
print(x1)

# random 產生0.0~1.0之間的3個亂數
x2 = np.random.random(3)
print(x2)

# rand 產生0.0~1.0之間的1個亂數
x3 = np.random.rand()
print(x3)

# rand 產生0.0~1.0之間的3個亂數
x4 = np.random.rand(3)
print(x4)

# rand(row, column) 產生亂數值陣列
x5 = np.random.rand(3, 2) # 3列,2行
print(x5)

# randint 產生 min 與 max 之間的整數亂數,不包括max
# randint(max, size)

# 建立 5~10之間的1個整數亂數
x6 = np.random.randint(5, 10)
print(x6)

# randint(min, max, size), min <= x < max

# 建立 1~11之間的10個整數亂數
x7 = np.random.randint(1, 11, size=10)
print(x7)

# 建立 1~11之間的4列5行陣列的整數亂數
x8 = np.random.randint(1, 11, size=(4, 5))
print(x8)

# 標準常態分配隨機樣本
# https://numpy.org/doc/stable/reference/random/generator.html

from numpy import random

# 舊版用法
vals = random.standard_normal(3)
print(vals)

more_vals = random.standard_normal(3)
print(more_vals)

# 新版用法
from numpy.random import default_rng

rng = default_rng()
vals = rng.standard_normal(3)
print(vals)

more_vals = rng.standard_normal(3)
print(more_vals)

##############################
# 5.7 陣列的屬性
##############################
import numpy as np

a = np.array([0,1,2,3,4,5])
a
a.dtype    # dtype('int32')
a.size     # 6
a.ndim     # 1
a.shape    # (6,)
a.itemsize # 4 bytes
a.nbytes   # 24

b = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10.]])
b
b.dtype    # float64
b.size     # 12
b.ndim     # 2
b.shape    # (3, 4)
b.itemsize # 8
b.nbytes   # 12*8=96

# 資料型別轉換
b.astype('int32')
b = b.astype('int32')
b.dtype    # int32

# 實作練習
# 建立3維陣列 myzero, 5個元素, 每個元素為3列,4行的零矩陣
# myzero.shape 結果為 (5, 3, 4)

##############################
# 5.8 一維陣列 - loop 處理
##############################

a = np.array([1,2,3,4])
a

# 方法1. array - 取出元素, 使用for
for x in a:
  print(x)

# 方法2. array - 取出元素, 使用while
i = 0
while i < len(a):
  print(a[i])
  i = i + 1

# 方法3. array - 取出元素, 使用指標 range, len
for i in range(len(a)):
  print(a[i])

# 方法4. array - 取出元素, 使用陣列包含法
[print(x) for x in a]

##############################
# 5.9 二維陣列 - loop 處理
##############################

a = np.array([[1,2,3,4], [5,6,7,8]])
a

for x in a:
  print(x)

for x in a:
    for item in x:
        print(str(item) + " ", end = " ")

##############################
# 5.10 陣列運算
##############################

a = np.array([1,2,3])
b = np.array([4,5,6])
a+b # 加
a-b # 減
a*b # 乘
a/b # 除

# 矩陣相乘(dot)
a = np.array([[1,2],[3,4],[5,6]])
a
b = np.array([[1,2],[3,4]])
b
a.shape # (3,2)
b.shape # (2,2)
c = a.dot(b) # 矩陣相乘(dot)
c

np.transpose(c) # 矩陣轉置
c.T             # 矩陣轉置

# inv()：反矩陣,逆矩陣 (inverse matrix)
from numpy.linalg import inv

x = np.array([[1, 2], [3, 4]])

inv(x)
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])

# 單位矩陣 (Identity matrix)
x.dot(inv(x))
# array([[1.00000000e+00, 1.11022302e-16],
#        [0.00000000e+00, 1.00000000e+00]])

x.dot(inv(x)).round(1)
# array([[1., 0.],
#        [0., 1.]])

# 計算矩陣行列式值 (determinant)
np.linalg.det(x)
# -2.0000000000000004

# 計算方形矩陣的特徵值 (eigenvalue) 與特徵向量 (eigenvector)
np.linalg.eig(x)
# 特徵值: (array([-0.37228132,  5.37228132]),
#  array([[-0.82456484, -0.41597356],
#         [ 0.56576746, -0.90937671]]))

##############################
# 5.11 reshape 應用
##############################
import numpy as np

z = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
z
z.reshape(-1) # -1: unknown dimension
# array([ 1,  2,  3, ..., 10, 11, 12])

z.reshape(-1,1) # row -1: unknown , column 1

z.reshape(-1, 2) # row -1: unknown , column 2

z.reshape(1,-1) # row 1 , column: unknown

z.reshape(2, -1) # row 2 , column: unknown

z.reshape(3, -1) # row 3 , column: unknown

z.reshape(-1, -1) # ERROR

##############################
# 5.12 建立副本
##############################

# 建立副本-使用等號
a = np.array([0,1,1,2,3,5])
b = a.reshape((3,2)) # b之修改會影響a
b

b.ndim   # 2
b.shape  # (3,2)

b[1][0] = 168
b
a # a物件已經更改, array([  0,   1, 168,   3,   4,   5])

# 建立副本-使用 copy
c = a.reshape((3,2)).copy()
c
c[0][0] = -999
c
a # a物件沒有更改

##############################
# 5.13 向量化處理
##############################

a = np.array([0,1,1,2,3,5])

a*2

a**3 # 次方運算
# end
