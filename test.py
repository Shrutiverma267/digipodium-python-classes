nums = set([1,1,2,3,3,3,4,4])
print(len(nums))
d = {"john":40,"peter":45}
print(list(d.keys()))
print("hello {0} and {1} ".format('foo','bin'))
a = {i:i*i for i in range(6)}
print(a)
s = 'digipodium'
slice = s[4:len(s)]
print(slice)
name1= ['amir','bala','chales']
if 'amir' in name1:
    print(1)
else:
    print(2)
print("ab\tcd\tef".expandtabs())
a = [13,56,17]
a.append([87])
a.extend([45,67])
print(a)
a=(1,2,3)
b = ('a','b','c')
d = tuple(zip(a,b))
print("abc.DEF".capitalize())

a = (2,3,1,5)
a.sort()
print(a)
a = "welcome to python".split()
a = (1,2,(4,5))
b = (1,2,(3,4))
a<b
