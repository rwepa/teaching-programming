"""
File     : 12_seaborn_visualization.py
Title    : 第12章 seaborn 視覺化
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

# 散佈圖矩陣 pairplot {seaborn}
# https://seaborn.pydata.org/
# seaborn-data: https://github.com/mwaskom/seaborn-data

# 安裝 seaborn 模組
import seaborn as sns

sns.set(style="ticks")

df = sns.load_dataset("iris")
df
#      sepal_length  sepal_width  petal_length  petal_width    species
# 0             5.1          3.5           1.4          0.2     setosa
# 1             4.9          3.0           1.4          0.2     setosa
# 2             4.7          3.2           1.3          0.2     setosa
# 3             4.6          3.1           1.5          0.2     setosa
# 4             5.0          3.6           1.4          0.2     setosa
# ..            ...          ...           ...          ...        ...
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica
# [150 rows x 5 columns]

sns.pairplot(df, hue="species")

###
# Question:
# import seaborn as sns 
# --> ImportError: DLL load failed: 找不到指定的程序。

# Solution: 可能是 scipy 或是 numpy 的版本問題, 移除後重新安裝
# conda remove numpy
# conda install numpy
# conda install seaborn
