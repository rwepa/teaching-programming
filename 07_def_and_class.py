"""
File     : 07_def_and_class.py
Title    : 第7章 函數與類別應用
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

##############################
# 大綱
##############################
# 7.1 函數(def)
# 7.2 類別(class)

##############################
# 7.1 函數(def)
##############################

# 回傳 a/b 之商數與餘數
def divide(a,b):
	q = a/b
	r = a - q*b
	return q,r

x, y = divide(42,5) 	# x = 8, y = 2
print(x)
print(y)

##############################
# 7.2 類別(class)
##############################

# 範例1
# 建立類別 class
class MyClass:
  x = 5

# 使用 () 實作實例
p1 = MyClass()
print(p1.x)

# 範例2
# __init__() 函數表示類別初使化時,該函數會自動執行, 左右為二個底線
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p1

print(p1.name)
print(p1.age)  

# 範例3
# Inheritance 繼承
# 父類別(Parent class)是給其他繼承的類別, 稱為基本類別.
# 子類別(Child class )是從另一個父類別繼承的, 也稱為衍生類別(derived class).
# https://www.w3schools.com/python/python_inheritance.asp

# 父類別
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("ALAN", "LEE")
x.printname()

# class 子類別(父類別)
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# 新增 __init__ 函數
# 子類別的__init __()函數將覆蓋父類別的__init __()函數
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# super - 表示使用父類別的方法
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Big", "Data")
x.printname()
# end
