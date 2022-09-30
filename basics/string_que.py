# 1
my_string = 'My name is Shruti'
print(my_string)

# 2 
name = input("Enter your name: ")
print(len(name))

# 3 
a = 'Python is great'
print(a[10:15])

# 4
word = '''Python 
is
everywhere.'''
print(word)

# 5
my_str = 'Hello World!'
print(my_str[::-1])

# 6
d = 'How are you?'
print('upper=>',d.upper())

# 7 
e = 'HOW IS IT GOING?'
print('lower=>',e.lower())

# 8 
words = ['Python','is','easy','to','learn']
content = "()".join(words)
print(content)

# 9 
my_string = ''' Python is easy
to learn 
and to use it.'''
result = " ".join(line.strip()for line in my_string.splitlines())
print(repr(result))

# 10 
my_string = "to move to nweline  '//n' is used"
print(my_string)

# 11
a = 15
print("the variable is,",a)


# 12
s1 = 'Python'
s2 = 'is'
s3 = 'great.'
s4 = s1+s2+s3
print(s4)
s5 = s1 + ' ' + s2 + ' ' + s3 
print(s5)

# 13
print('#' * 20)

# 14
for i in range(1,10):
    print(i,'.',sep=' ')

# 15
sente = input("Enter a sentence:") 
print(* sente.split(" "),sep= '\n')

# 24
text = '%p34@y!*-*!t68h#&on404'
from string import punctuation
for p in punctuation:
    text = text.replace(p, '')
from string import digits
remove_digits = str.maketrans('','',digits)
res = text.translate(remove_digits)
print(res)

# 23
msg = input("Enter a string:")
if "fyi" in msg:
    print("Yes! it is present in the string")
else :
    print("No! it is not present")

# 21
names = 'joe,david,mark,tom,chris,robert'
l=[]
l=names.split(',')
print(l)

# 22
text = 'this is some text'
a = text.split( )
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)


# 16
message = input('Enter a string:')
print(message.endswith('?'))

# 17
z = input("Enter a string:")
num_of_in = z.count('e')
print(f'e occurs {num_of_in} times')

# 18
integer = input("Enter something:")
if integer.isdigit():
    print("is a number")

    user_inp = int(integer)
else:
    print("not a number")

# 19
text = '    this is not a good string   '
cleaned_text = text.strip()
print(cleaned_text)

# 20
textt = input("enter text:")
if textt.isupper():
    print("Found")
else:
    print("Not Found")

# 25
sentence = input("Enter the sentence:")
words = sentence.split()
count = 0
sum = 0
for x in words:
    sum += len(x)
    count += 1
total = sum / count
print(total)