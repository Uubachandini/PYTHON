"""
list is a collections/group of items/values/elements
they can be enclosed within the square brackets[] seperated by(,)
list methods: append/extend/count/mutability/index/remove/pop/insert
syntax:listname.methodname()

"""
#append: this method is used to add the elements
# list1=[ "india", "scotland", "spain"]
# print(list1)
# list1.append("london")
# print(list1)

# # extend:this method is used to add the elements at the end but
# # as a sublist

# list2=[ "guava", "orange", "apple", "kiwi"]
# print(list2)
# list2.extend( ["grapes", "dragon","pineapple", "blueberry"])
# print(list2)

#count: this method counts the number of repeated elements in a list
# flowers=[ "rose","sunflower", "jasmine", "mariegold", "lotus"]
# flowers.count(("rose"))
# print(flowers)

#Mutabilitychanging the elements..
# mylist4=["hello","ECE",123,36.56,65+5j]
# print(mylist4)
# mylist4[2]="Agri"
# print(mylist4)

#Pop: Removes the elements user index
# mylist5=[12,34,565,76.9,34+56j,"hello"]
# print(mylist5)
# mylist5.pop(2)
# print(mylist5)

#remove:remove the element directly that are present in a list
# mylist5.remove(34)
# print(mylist5)

#count: it counts the number of occurance of a item in a list
#Note:count method takes a one argument at a time
# mylist6=[22,33,33,22,55,22,44,67,56,22]
# print(mylist6.count(22))

#insert: it just insert the elements into the list using the index
# mylist7=[22,33,44,77,88]
# print(mylist7)
# mylist7.insert(1,"Hello")
# print(mylist7)
#Note:In insert method no element is removed they just replace the position

#Index:This method tells the index of first occurance of a element
mylist8=[22,44,55,55,44,66,67,89]
print(mylist8.index(44))
print(mylist8.index(55))

#reverse--ift just copy the elements in a list
mylist8.reverse()
print(mylist8)
#copy=it just copy the elements in a list from one list to another
mylist9=[22,33,44,55,66,77]
print(mylist9)
mylist10=mylist9.copy()
print(mylist10)
#clear--it cleary the element is a list
print(mylist10.clear(()))
print(mylist10)

#sort--it just arrange the elemets in sorting array
mylist11=[22,11,77,9,89,8]
mylist11.sort()
print(mylist11)
mylist12=["a","a","k","b","c","d","j","f"]
mylist12.sort()
print(mylist12)
mylist13=[12,123,"Hello"]
mylist13.sort()
#in buit functions 
mylist12=[23,34,56,89]
print(len(mylist12))
print(max(mylist12))
print(max(mylist12))
print(sum(mylist12))