
#Datetypes indicates the types of the data that a variable is holding on 
'''
DATATYPES:
Number 
sequence
boolean
set
dictionary
 '''
''' 
Number is divided into 3 types 
1) Integer 
2) Float 
3) Complex '''

# a=123
# print(a)
# print(type(a))
# print(id(a))

# a1=-98
# print(a1)
# print(type(a1))
# print(id(a1))
''' 
type()... which tells about the type of a value that internally compiler holding on
id().... which tells about the address  of a value 
'''

# b=89.456
# print(b)
# print(type(b))
# print(id(b))


# b1=-89.456
# print(b1)
# print(type(b1))
# print(id(b1))

'''
complex datatypes are used to hold the real and imaginary value 
which can be represented as a+bj '''

# c=78+67j
# print(c)
# print(type(c))
# print(id(c))

# c1=-456+56j
# print(c1)
# print(type(c1))
# print(id(c1))


'''
sequence datatypes are divided into 3 types 
1) string 
2) list 
3) tuple 

string means group of / collection of characters 
it can be enclosead using the single quotes or double quotes  
'''

# a="ISTS"
# print(a)
# print(type(a))
# print(id(a))

# b='chandini'
# print(b)
# print(type(b))
# print(id(b))


'''
list: it is  a collection of items / values / elements
syntax: listname=[ value1, value2, value3.... valuen]
list is mutable (internal values can change automatically)'''
 
# mylist=[20,20.36,3+6j,"hello"]
# print(mylist)
# print(type(mylist))
# print(id(mylist))
# print(mylist[1])
# print(mylist[3])
'''
in order to aacess the elements individual we use indexing 
iindexing always starts with "0" ends with n-1 
syntax to access the elements 
print(listname(element position))'''

'''
tuple : it is a collection of items/values/elements
syntax: tuplename=(vale1,value2,value3,.....value )
tuple is unmutable (internal values can't change automatically)'''

# mytuple=(63,56.7,4+5j,"hi madam")
# print(mytuple)
# print(type(mytuple))
# print(id(mytuple))
# print(mytuple[2])
# print(mytuple[0])
'''
Giving a list within a list is called sublist
GIVING A TUPLE within a tuple is called subtuple 
'''
'''
boolean: boolean means checks the condition 
they are divided to two ways 1.True 2.False 
it can be represented as bool''' 


# a=True
# print(a)
# print(type(a))

# b=False
# print(b)
# print(type(b))
'''
 set: it is a collection of values/items/elements
 syntax: setname{val1,val2....valn}
 a set can't accept the list'''

# myset={23,45.6,"hello",(143,"chandini"), True}
# print(myset)

'''
dictionary: It is a collection of key value pairs
syntax: dictionaryname={KEY1:val1,key2:val2.....keyn:valn}'''

mydict={1:"ists","branch":"ECE","Rollno":"0490"}
print(mydict)
print(type(mydict))