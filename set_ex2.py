#set union
a = {1,2,3,4,5}
b = {4,5,6,7,8}
# use | operator
print(a|b)
#use unionn function
a.union(b)
#use union function on b
b.union(a)

# set intersection
a = {1,2,3,4,5,}
b = {4,5,6,7,8}
#use & operator
print(a&b)
a.intersection(b)

#set difference 
print(a-b)

#use difference function on a
a.difference(b)

#use - operator on b
b - a
print(b-a)