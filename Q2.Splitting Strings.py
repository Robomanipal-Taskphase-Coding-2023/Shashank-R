from itertools import permutations

def Combinations(sentence):
    c_lis = list(sentence.split())
    order = permutations(c_lis)

    for i in order:
        o_list = list(i)
        for j in o_list:
            print(j, end = " ")
        print()
 
 
print("All Possible Combinations Of Words!")
sentence=input("Input a string:")
Combinations(sentence)
