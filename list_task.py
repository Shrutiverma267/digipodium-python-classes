names = []
for i in range(5):  #1
    names.append(input('enter a name=>'))
for name in names:
    print(name[::-1])

#2 wap to print a fibonacci series using the concept of list
fib = [0,1]
for i in range(15):
    fib.append(fib[-1] + fib[-2])
print(fib)

#3 wap to generate a new list that contains squares of each from list
x =[1,2,3,3,4,5,6,7]
x2 = []
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

#4 add odd numbers
x = [1,2,3,3,4,5,6,7]
xodd = []
for i in x:
    if i % 2 !=0:
        xodd.append(i)
print(xodd)

#5 adding 2 list elementwise
x = [1,2,3,4,5,6]
y = [6,4,3,2,1,2]
z = []
for i,j in zip(x,y):
    x.append(i+j)
print(x)
print(y)
print(z)

#table
for i in range(1,11):
    print(f'2*{i} = {2*i}')


