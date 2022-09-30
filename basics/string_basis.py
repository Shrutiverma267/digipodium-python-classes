#defining strings in python
#all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

#triple quotes string can extend multiple lines
my_string = """Hello, welcome to
            the world of python"""
print(my_string)

a = 'Excalibur'
print(a)
b = "Smallfoot"
print(b)
c = '''Once upon 
a time, there was a person
that use to sleep.
the end'''
print(c)

print(a[0]) #first char
print(a[2]) #third char
print(a[-1])#last char
print(a[-3])#third last char
print(a[0],a[2])

name = 'vijay deenanath chauhan'
for i,c in enumerate(name):
    print(i,c)
mname = name[6: -8]
print(mname)
print(name[6: -8])
fname = name[:5]
print(fname)

lname = name[-7:]
print(lname)
sname = name[11:-8]
print(sname)

#reverse the string
print(name[::-1])
print(name[:5][::-1])

#every even idx char
print(name[::2]) #vjy
#every odd idx char
print(name[::3]) 
print(name[1::2])


x = chr(65)
print(x)
x = chr(2365)
print(x)
x = chr(12365)
print(x)
for i in range(15000,20000):
    print(i,chr(i))

y = ord('A')
print(y)
y = ord('a')
print(y)
y = ord('{')
print(y)

a = 'apple'
b = 'juice'
ab = a+b
print(ab)

w1 ='this'
w2 = 'is'
w3 = 'Amazing'
msg = w1+w2+w3
print(msg)

#adding space b/w string
msg = w1 + ' ' + w2 + ' ' + w3
print(msg)

#duplication
word = 'Hi'
print(word * 3)
print('-' * 25)