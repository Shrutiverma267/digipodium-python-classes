# set cannot have duplicates
my_set= {1,2,3,4,3,4}
print(my_set)
# we can make a set from a list
my_set = set([1,2,3,2])
print(my_set)
#my_set={1,2,[3,4]}
#print(my_set)

#initialize a with set()
#a = set()
#print(type(a))

#initialize my set
my_set = {1,3}
print(my_set)

#add an element
my_set.add(2)
print(my_set)

#add multiple elements
my_set.update([2,3,4])
print(my_set)

#add list and tuple
my_set.update([4,5],{1,2,3})
print(my_set)

# initialize my set
my_set = {1,3,4,5,6}
print(my_set)

#discard an element
my_set.discard(4)
print(my_set)

#remove an element
my_set.remove(6)
print(my_set)

#pop a random element
my_set.pop()
print(my_set)

#clear my set
my_set.clear()
print(my_set)