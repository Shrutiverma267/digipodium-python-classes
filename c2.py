class Cat:
    # constructor
    def __init__(self, name, age, breed):
        #syntax for instance_variable
        #self.<attribute> = <parameter>
        self.name = name
        self.age = age
        self.breed = breed

cat1 = Cat('soni', 3, 'persian')
cat2 = Cat('mia', 2, 'siamese')
cat3 = Cat('molly', 4, 'egyptian mau')

print(cat1.name,cat1.age,cat1.breed)
print(cat2.name,cat2.age,cat2.breed)
print(cat3.name,cat3.age,cat3.breed)