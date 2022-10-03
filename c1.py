# class definition
class Dog:
    #pass
    breed = 'labrador'
    age = 3
    name = 'tommy'

# object instantiation
dog1 = Dog()
dog1.name = 'sheru'
dog1.age = 5
dog1.breed = 'german shepherd'

dog2 = Dog()
dog2.name = 'rex'
dog2.age = 2
dog2.breed = 'golden retriever'

dog3 = Dog()
dog3.name = 'buddy'
dog3.age = 4
dog3.breed = 'pug'


print(dog1.name,dog1.age,dog1.breed)
print(dog2.name,dog2.age,dog2.breed)
print(dog3.name,dog3.age,dog3.breed)