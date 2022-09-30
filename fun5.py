def marks(**data):
    with open('marks.txt','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}\n')

marks(rajesh=200,brijesh=120)
marks(raj=130,ajay=90,shruti=120,lucky=150)
marks()