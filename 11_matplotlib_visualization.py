"""
File     : 11_matplotlib_visualization.py
Title    : 第11章 matplotlib 視覺化
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

# 大綱
# 11.1 matplotlib常用語法
# 11.2 水雷 vs. 岩石 視覺化分析

# 11.1 matplotlib常用語法
import matplotlib.pyplot as plt
import numpy as np

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 半徑 0~15

# 散佈圖 plt.scatter
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.savefig('random.plot.png')
plt.savefig('random.plot.pdf')
plt.show()

plt.scatter(x, y, s=500, c=colors, alpha=0.5)
plt.show()

# 線圖 plt.plot
plt.plot(x,y)

plt.plot(sorted(x), y)

# example 1 - 線圖
plt.plot([1,2,3,4])   # x 軸: 0,1,2,3
plt.ylabel("Quality")
plt.show()

# example 2 - 點圖
plt.plot([1,2,3,4], [1,4,9,16], 'ro')  # r:red, o:circle marker
plt.axis([0, 6, 0, 20]) # set xlim and ylim
plt.show()

# example 3 - 3組資料
t = np.arange(0., 5., 0.2) # 等差級數, 區間包括啟始, 不包括結束
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# example 4
plt.figure(1)                # the first figure

# 211: (nrow, ncol, plot_number) 
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

# example 5
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# example 6 直方圖 (histogram)
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(123)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(50, 0.025, r'$\mu=100,\ \sigma=15$', size = 50)
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()

# example 7 多列多行繪圖
fig = plt.figure()

# subplot:設定圖形位置(列,行,編號)
# fig.add_subplot(221)   #top left
# fig.add_subplot(222)   #top right
# fig.add_subplot(223)   #bottom left
# fig.add_subplot(224)   #bottom right 
# plt.show()

# plt.subplot()
# subplot(232) # 2列, 3行, 圖2位置
# 圖1 , 圖2 , 圖3
# 圖4 , 圖5 , 圖6

# color
"""
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""
# https://matplotlib.org/users/colors.html

# line style or marker
"""
'-'	  solid line style
'--'	  dashed line style
'-.'	  dash-dot line style
':'	  dotted line style
'.'	  point marker
','	  pixel marker
'o'	  circle marker
'v'	  triangle_down marker
'^'	  triangle_up marker
'<'	  triangle_left marker
'>'	  triangle_right marker
'1'	  tri_down marker
'2'	  tri_up marker
'3'	  tri_left marker
'4'	  tri_right marker
's'	  square marker
'p'	  pentagon marker
'*'	  star marker
'h'	  hexagon1 marker
'H'	  hexagon2 marker
'+'	  plus marker
'x'	  x marker
'D'	  diamond marker
'd'	  thin_diamond marker
'|'	  vline marker
'_'	  hline marker
"""

# 11.2 水雷 vs. 岩石 視覺化分析

import pandas as pd
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 資料: 208列, 61行
# X: V0-V59
# Y: V60
# 第61行: R: rock  岩石
# 第61行: M: mine 水雷

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
rocksVMines
#          V0      V1      V2      V3      V4  ...     V56     V57     V58     V59  V60
# 0    0.0200  0.0371  0.0428  0.0207  0.0954  ...  0.0180  0.0084  0.0090  0.0032    R
# 1    0.0453  0.0523  0.0843  0.0689  0.1183  ...  0.0140  0.0049  0.0052  0.0044    R
# 2    0.0262  0.0582  0.1099  0.1083  0.0974  ...  0.0316  0.0164  0.0095  0.0078    R
# 3    0.0100  0.0171  0.0623  0.0205  0.0205  ...  0.0050  0.0044  0.0040  0.0117    R
# 4    0.0762  0.0666  0.0481  0.0394  0.0590  ...  0.0072  0.0048  0.0107  0.0094    R
# ..      ...     ...     ...     ...     ...  ...     ...     ...     ...     ...  ...
# 203  0.0187  0.0346  0.0168  0.0177  0.0393  ...  0.0065  0.0115  0.0193  0.0157    M
# 204  0.0323  0.0101  0.0298  0.0564  0.0760  ...  0.0034  0.0032  0.0062  0.0067    M
# 205  0.0522  0.0437  0.0180  0.0292  0.0351  ...  0.0140  0.0138  0.0077  0.0031    M
# 206  0.0303  0.0353  0.0490  0.0608  0.0167  ...  0.0034  0.0079  0.0036  0.0048    M
# 207  0.0260  0.0363  0.0136  0.0272  0.0214  ...  0.0040  0.0036  0.0061  0.0115    M

# print head and tail of data frame
print(rocksVMines.head())
rocksVMines.tail()

# print summary of data frame
summary = rocksVMines.describe()
print(summary)
#                V0          V1          V2  ...         V57         V58         V59
# count  208.000000  208.000000  208.000000  ...  208.000000  208.000000  208.000000
# mean     0.029164    0.038437    0.043832  ...    0.007949    0.007941    0.006507
# std      0.022991    0.032960    0.038428  ...    0.006470    0.006181    0.005031
# min      0.001500    0.000600    0.001500  ...    0.000300    0.000100    0.000600
# 25%      0.013350    0.016450    0.018950  ...    0.003600    0.003675    0.003100
# 50%      0.022800    0.030800    0.034300  ...    0.005800    0.006400    0.005300
# 75%      0.035550    0.047950    0.057950  ...    0.010350    0.010325    0.008525
# max      0.137100    0.233900    0.305900  ...    0.044000    0.036400    0.043900

#平行座標軸 Parallel coordinates graph
for i in range(208):
    # assign color based on color based on "M" or "R" labels
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"

    # plot rows of data as if they were series data
    dataRow = rocksVMines.iloc[i, 0:60]
    plot.rcParams["figure.figsize"] = (20, 15) #(寬, 高)
    dataRow.plot(color=pcolor, alpha=0.5)
    # plot.figure(figsize=(16, 16))

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()
# end
