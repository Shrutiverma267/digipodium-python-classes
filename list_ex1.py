movies = ['Sholay','Baghban','DDLJ','Ironman'
         ,'RRR','Inception','Kung Fu Panda','Spiderman',
         'Suryavansham','Batman']
print(len(movies))
print(movies)
movies.sort()
print(movies)
movies.reverse()
print(movies)
print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print("all movies except first three",movies[3:])
print('movies with even indexes',movies[::2])
