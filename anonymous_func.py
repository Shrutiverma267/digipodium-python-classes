nums = [1,2,3,4,1,2,3,5,6,7,3,3,2,1,2,3,5,6,]
names = ['ajay singh','vijay pratap','lucky thakur']

num_sqr = list(map(lambda i:i**2,nums))
print(num_sqr)

num_eqi = list(map(lambda i:i+4 * i**2,nums))
print(num_eqi)

first_names = list(map(lambda nm:nm.split()[0],names))
print(first_names)