def second_largest(list):
    list.sort()
    return list[-2]

s_list=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
    ele=int(input("Enter element of list: "))
    s_list.append(ele)

print("second largest in ",s_list,"is: ")
print(second_largest(s_list)) 
