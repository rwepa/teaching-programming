"""
File     : 08_scipy_calculus_interpolation.py
Title    : 第8章 scipy模組_微積分,內插法
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

##############################
# 大綱
##############################

# 8.1 sympy 模組簡介
# 8.2 scipy 模組簡介
# 8.3 內插法

##############################
# 8.1 sympy 模組簡介
##############################

# 極限 --> 近似值  lim_x-->a f(x)=L, 表示當 x 愈趨近 a， ƒ(x) 就愈趨近 L。
# 左邊極限 = 右邊極限, 則極限才存在.
# 微分 --> 切線斜率
# 積分 --> 面積

# 函數 ƒ 對 x 的導函數 (微分)為  ƒ’，定義為f'(x)=lim_Δx-->0 ( f(x+Δx)-f(x) )/Δx

# sympy 模組
# SymPy is a Python library for symbolic mathematics(符號計算). It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python.
# https://www.sympy.org/

# 功能: 多項式, 微積分, 微分方程, 矩陣, 物理(機械,量子), 統計, 密碼學
# https://www.sympy.org/en/features.html

# sympy功能簡介
# https://docs.sympy.org/latest/tutorial/calculus.html

# 極限
from sympy import limit, diff, cos, exp, integrate
from sympy.abc import x, y

limit(1/x, x, 0) # default dir='+', 右極限 = ∞
limit(1/x, x, 0, dir="-") # 左極限 = -∞
# 因為左極限不等於右極限, 因此f(x)=1/x 在 x = 0 極限不存在

limit((x**2 + x -12)/(x-3), x, 3) # 右極限 = 7
limit((x**2 + x -12)/(x-3), x, 3, dir="-") # 左極限 = 7
# 因為左極限等於右極限, 因此f(x) 在 x = 3 極限存在=7

# 微分
diff(x**4 + 2*x**3, x) # 預設為1階微分

diff(x**4 + 2*x**3, x, x, x) # 3階微分, 使用x符號表示

diff(x**4 + 2*x**3, x, 3) # 3階微分, 使用參數3表示

diff(exp(x**2), x)

# 積分
integrate(6*x**5, x)

# 多變數積分
integrate(x*y, x)

# 定積分
integrate(x**3, (x, -1, 1))
 
# 轉換為泰勒展開式 (Taylor series)
cos(x).series(x, 0, 10)

##############################
# 8.2 scipy 模組簡介
##############################

# scipy 模組
# https://scipy.org/

# scipy 模組六大特性
# 1.FUNDAMENTAL ALGORITHMS(基礎演算法) 
# SciPy provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other classes of problems.

# 2.BROADLY APPLICABLE(廣泛應用)
# The algorithms and data structures provided by SciPy are broadly applicable across domains.

# 3.FOUNDATIONAL(基礎)
# Extends NumPy providing additional tools for array computing and provides specialized data structures, such as sparse matrices and k-dimensional trees.

# 4.PERFORMANT(高效能的)
# SciPy wraps highly-optimized implementations written in low-level languages like Fortran, C, and C++. Enjoy the flexibility of Python with the speed of compiled code.

# 5.EASY TO USE(容易使用)
# SciPy’s high level syntax makes it accessible and productive for programmers from any background or experience level.

# 6.OPEN SOURCE(開放源始碼)
# Distributed under a liberal BSD license, SciPy is developed and maintained publicly on GitHub by a vibrant, responsive, and diverse community.

# 參考資料
# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html#general-integration-quad

import scipy.integrate as integrate
import numpy as np

help(integrate)

# scipy.integrate 三大功能
# 1.General integration (quad) 積分- quad
# 2.數值積分法 
#   trapezoidal rule 梯形法則 - trapz
#   Simpson‘s rule 辛浦森法則 - simps 
# 3.微分方程 ordinary differential equations - odeint 

# 定積分-範例1
myfunction = lambda  x: np.sin(x)
result = integrate.quad(myfunction, 0, np.pi)
result # 定積分結果, absolute error

# 定積分-範例2
result1 = integrate.quad(lambda x: x**3, -1, 1)
result1

# 定積分-範例3
myf = lambda x: x**2 + x + 1
result2 = integrate.quad(myf, 1, 4)
result2

# 梯形法則(trapz) - 範例
from scipy.integrate import trapz, simps
import numpy as np

def f1(x):
   return np.sin(x)

x1 = np.linspace(0, np.pi, 5)
x1

trapint = trapz(f1(x1), x1)
print(trapint)

sinint = simps(f1(x1), x1)
print(sinint)

x2 = np.linspace(0, np.pi, 9)
x2

trapint = trapz(f1(x2), x2)
print(trapint)

sinint = simps(f1(x2), x2)
print(sinint)

# 多重積分 Multiple integral
from scipy import integrate
x = np.arange(0, 10)
y = np.arange(0, 10)
integrate.simps(y, x)

##############################
# 8.3 內插法
##############################

# 內插法 Interpolation (插值法)
# https://en.wikipedia.org/wiki/Interpolation

# Nearest-neighbor interpolation 近鄰插值法
# Linear interpolation           線性插值法
# Polynomial interpolation       多項式插值法
# Spline interpolation           樣條插值法

# scipy.interpolate 
# https://docs.scipy.org/doc/scipy/reference/interpolate.html

##############################
# interp1d - nearest, previous, next (近鄰插值法)
##############################

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

fnearest = interp1d(x, y, kind='nearest') # 近鄰法,參考y座標最近距離之資料點
fprevious = interp1d(x, y, kind='previous') # 前端點法
fnext = interp1d(x, y, kind='next') # 後端點法

xnew = np.linspace(0, 10, num=1001, endpoint=True)

plt.plot(x, y, 'o')
plt.plot(xnew, fnearest(xnew), '-', 
         xnew, fprevious(xnew), '--', 
         xnew, fnext(xnew), ':')
plt.legend(['data', 'nearest', 'previous', 'next'], loc='best')
plt.title('nearest, previous, next method')

##############################
# interp1d - cubic (線性插值法, 樣條插值法)
##############################

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

f1 = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)

plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
# end
