salary = int(input("enter ur salary:"))
if salary>100000:
    print("da=3.5%,hra=9.1%")
    Da = (salary*3.5)/100
    hra = (salary*9.1)/100
    print("final salary",salary-da-hra)
elif salary > 80000:
    print("da=3.2%")
