def getBinaryForm(decimalnum):
    if decimalnum == 0:
        return 0
    else:
       return (decimalnum % 2 + 10 * getBinaryForm(int(decimalnum // 2)))

print("Converting Decimal to Binary! ")
decimalnum = int(input("Enter an Integer:"))
print("The binary equivalent of",decimalnum,"is:")

print(getBinaryForm(decimalnum))
