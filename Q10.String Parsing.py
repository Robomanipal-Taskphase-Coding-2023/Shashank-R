def finaldict():
    x=str(input("Enter string:"))
    p=x[::-1]
    a=""

    for i in range(len(p)):
        if p[i]=="0":
            a=a+p[0:i]
            b_id=a[::-1]
            c_firstname=""
            for i in range(len(x)):
                if x[i]=="0":
                    c_firstname=c_firstname+x[0:i]
                    e=x.replace(c_firstname,"")
                    w=""
                    o_lastname=""
                    for i in range(len(e)):
                        if e[i].lower() in "abcdefghijklmnopqrstuvwxyz":
                            w=e[i::]
                    for j in range(len(w)):
                        if w[j]=="0":
                            o_lastname=w[0:j]

    finaldict={"first_name": c_firstname, "last_name": o_lastname, "id": b_id}
    return finaldict()
finaldict()

