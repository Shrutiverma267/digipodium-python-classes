name = input("enter name of emp:")
days = int(input("enter no of days present:"))
wages = int(input("enter wages per day:"))
sal = wages*days
if sal > 100000:
    hra = sal*9.1
    da = sal*3.5
    finalsalary = sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 80000:
    hra = sal * 9
    da = sal * 3.2
    finalsalary = sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 60000:
    hra = sal * 9
    da = sal * 2.8
    finalsalary = sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 50000:
    hra = sal *8
    da = sal*2.5
    finalsalary= sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 40000:
    hra = sal*7.7
    da = sal*2.5
    finalsalary = sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 30000:
    hra = sal*8
    da = sal*2.2
    finalsalary= sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 20000:
    hra = sal*7
    da = sal*2.2
    finalsalary= sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))
elif sal > 10000:
    hra = sal*6
    da = sal*2.2
    finalsalary= sal+hra+da
    print("\nsal:%1f \nhra:%1f \nda:%1f \nfinalsalary:%1f" %(sal,hra,da,finalsalary))

