def divisible(num1, num2):
    div_list = []
    for i in range(num1, num2+1):
        if (i%7==0) and (i%5!=0):
            div_list.append(i)
    result = ','.join([str(i) for i in div_list])
    return result
num1 = 2000
num2 = 3200
print("Numbers Divisible by 7 But Not by 5!")
print(divisible(num1,num2))
