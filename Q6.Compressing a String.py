
def ischar(c):
	return ord(c) >= 48 and ord(c) <= 57


def checkCompressed(S, T):
    i,j = 0,0
    while (j < len(S) and i < len(T)):
        if (isnum(T[i]) == False):
            if (S[j] != T[i]):
                return 0
                j += 1
            else:
		ans = ord(T[i]) - 48
		i += 1
                while (i < len(T) and isnum(T[i])):
                    ans *= 10
                    ans += T[i] - 48
                    i += 1
		j += ans
		i -= 1

	    i += 1

		
	if (j != len(S)):
		return 0

	return 1


print("Compressing a String!")
S =input("Input String:")
T =input("Input Compressed String;")
print(checkCompressed(S, T))


