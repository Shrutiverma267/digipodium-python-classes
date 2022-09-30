from pprint import pp
movies = {}
movies['top gun:marvick'] = 8.3
movies['rrr']= 8.1
movies['spiderman:no way home']=8.2
#pp(movies)

for item in movies:
    print(item)

print('only values')
for item in movies:
    print(movies[item])

print('both key and values')
for key in movies:
    print(key,movies[key])

print('using dict.items() method')
for k,v in movies.items():
   print(k,v)


#user input 
for i in range(3):
    name = input("movies name:")
    rating = float(input("movies rating:"))
    movies[name]= rating 

print('using dict.items()method')
for k,v in movies.items():
    print(k,v)