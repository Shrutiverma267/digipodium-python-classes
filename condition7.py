num=int(input('enter a number: '))

match num:
     case _:
    print('sunday')
    case _:
    print('monday')
    case _:
    print('tuesday')
    case _ :
    print('wednesday')
    case _: #_char act as a default, if none of the cases match
    print('invalid data')