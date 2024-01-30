a={1 :'abc', 2:'def', 3:'ghi'}
print(a)

# we can create empty dictionry
b={}
print(b)
b[1]='abc'
print(b)

#retrieving the value using key
print(b[1])

#retrieving only key
print(a.keys())

#retrieving only values
print(a.values())

#updating the value of any particular key
b[2] = 'rahul'
print(b)

#deleting the element
del b[2]
print(b)