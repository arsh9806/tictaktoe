'''import json
Sandeep = 1,2,3,4,5, 6
print(Sandeep,hex(id(Sandeep)),type(Sandeep))
print(Sandeep,oct(id(Sandeep)))

zomatoDiscout = 40
print(zomatoDiscout, hex(id(zomatoDiscout)))

print()

zomatoDiscout = 4
print(zomatoDiscout, hex(id(zomatoDiscout)))
NewList = [1,2,3,4,5,6,8,9]
print(NewList,hex(id(NewList)),type(NewList))
#sets
NewSet = {1 , 2 , 3 , 3 }
NewSet.pop()
A = set("hello")
print(A)
print(NewSet)
print("h" in NewSet)
for i in A:
    print(i,end = " ")
#Dictionary in python
dictionary = { 100 : "one",200 : "two ", 300: " three"}
print(dictionary[200])
#json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.dumps(True)

# the result is a Python dictionary:
print(y,type(y))'''
SampleList = [1,2,3,4,5,6.6]
print(SampleList,hex(id(SampleList)),type(SampleList))
SampleList+=[4]
print(SampleList,hex(id(SampleList)),type(SampleList))