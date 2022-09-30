books = ['Steelheart','Firefight','osmosis','Calamity']
#[1::2]for odd no
books.append('The first Empire')
books.append('Atomic habit')
books.append('you can win')
books.append('three mistakes of my life')
print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[6] = 'The well of Ascension'  #update
books[-1] = 'the hero of ages'
books[2] = 'legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3, 'legion: Skin deep')
books.insert(5, 'Elantris')
print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('Steelheart')
books.remove('legion')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

#extend function
fruits = ['apple','banana','cherry','guava']
dry_fruits = ['almond','cashew','walnut']
fruits.extend(dry_fruits)
print(fruits)

#mixed data list not sort same type only work remove() work only 1 element one time


