def get_salary():
    val = int(input("enter amt:"))
    fine = .09
    return val * fine

print("salary",get_salary())

a = get_salary()
print('salary',a)

final_salary = get_salary() + 1000
print('salary',final_salary)

def amount():
    p = int(input('principle:')) 
    r = float(input('rate:'))
    t = int(input('time:'))
    si = p*r*t /100 
    amt = si + p
    return amt, si

amt,si = amount()
print(f'the amount will be {amt} on simple interest {si}')
# or this way
print(f'the amount will be {amount()[0]}')

def word_count(msg):
    words = msg.split()
    return len(words)

    word_count("this is time to go")