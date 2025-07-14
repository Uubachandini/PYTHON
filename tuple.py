"""
Tuples is a collection of items/values/elementsthey are enclosed within the perenthasis of 
open brackets separated by (,)As tuples are  imutable it mean we can't change 
so when  the data is fixed we can go to Tuple
"""

#eg1=
mytuple=(13,12,11)
print(type(mytuple))
mytuple1=()
print(type(mytuple1))
mytuple2=(10)
print(type(mytuple2))

"""
Note:when you wanna create a tuple with single vaule it should be sepersted by so that the complier 
treats at tuple or else or just treats as integer 
"""
#Creation of tuple
#syntax:tuplevariable=(value1,value2,....valueN)
mytuple4=(12,23.45,45+56j,[12,34,45],"Hello",(123,"ECE"))
print(mytuple4)

#creating the tuple with a single element
mytuple5=(45,)
print(type(mytuple5))

#creating a tuple with a list
t=[23,45,56,"KK"]
print(t)
k=tuple(t)
print(k)

#creating the tuple with "tuple" predefined word
t=tuple()#it consider as empty by tuple
print(t)