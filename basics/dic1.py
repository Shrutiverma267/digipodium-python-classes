# dictionary with integer keys 
my_dict = {1:'apple',2:'ball'}
print(my_dict)

val = ['rajendra singh',30,10,'accounts','staff officer',60000,7,]
val_dict = {
    'employee': 'rajendra singh','age':30,
    'experience':10,'dept':'accounts',
    'designation':'system officer','salary':60000,
    'team_size':7
}

#displaying a dict
print(val_dict)

#retrival of value
ans = val_dict['designation'] #key in []
print(ans)
print(val_dict['salary']) #correct
print(val_dict['experience']) #incorrect

#adding a data inside dict
val_dict['company'] = 'acme.inc'
print(val_dict)

from pprint import pp
pp(val_dict)