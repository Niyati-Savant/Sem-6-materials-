gram = {}
# def add(string):
#     string = string.replace(" ", "").replace("	", "").replace("\n", "")
#     x = string.split("->")
#     y = x[1]
#     x.pop()
#     z = y.split("|")
#     x.append(z)
#     gram[x[0]] = x[1]

def add(string):
    string = string.replace(" ", "").replace("\t", "").replace("\n", "")
    x = string.split("->")
    non_terminal = x[0]
    productions = x[1].split("|")
    gram[non_terminal] = [list(prod) for prod in productions]


def removeDirectLR(gramA, A):
    """gramA is dictionary"""
    temp = gramA[A]
    tempCr = []
    tempInCr = []
    for i in temp:
        if i[0] == A:
            # tempInCr.append(i[1:])
            tempInCr.append(i[1:] + [A + "'"])
        else:
            # tempCr.append(i)
            tempCr.append(i + [A + "'"])
    tempInCr.append(["e"])
    gramA[A] = tempCr
    gramA[A + "'"] = tempInCr
    return gramA


def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
    return False


def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t = []
                t += k
                t += i[1:]
                newTemp.append(t)

        else:
            newTemp.append(i)
    gramA[A] = newTemp
    return gramA


def rem(gram):
    c = 1
    conv = {}
    gramA = {}
    revconv = {}
    for j in gram:
        conv[j] = "A" + str(c)
        gramA["A" + str(c)] = []
        c += 1

    for i in gram:
        for j in gram[i]:
            temp = []
            for k in j:
                if k in conv:
                    temp.append(conv[k])
                else:
                    temp.append(k)
            gramA[conv[i]].append(temp)

    # print(gramA)
    for i in range(c - 1, 0, -1):
        ai = "A" + str(i)
        for j in range(0, i):
            aj = gramA[ai][0][0]
            if ai != aj:
                if aj in gramA and checkForIndirect(gramA, ai, aj):
                    gramA = rep(gramA, ai)

    for i in range(1, c):
        ai = "A" + str(i)
        for j in gramA[ai]:
            if ai == j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    op = {}
    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j], j)
        revconv[i] = a

    for i in gramA:
        l = []
        for j in gramA[i]:
            k = []
            for m in j:
                if m in revconv:
                    k.append(m.replace(m, revconv[m]))
                else:
                    k.append(m)
            l.append(k)
        op[revconv[i]] = l

    return op


n = int(input("Enter No of Production: "))
for i in range(n):
    print("Enter rule in A -> aA|B form")
    txt = input()
    add(txt)

result = rem(gram)

for x, y in result.items():
    print(f'{x} -> ', end="")
    for index, i in enumerate(y):
        for j in i:
            print(j, end="")
            if index != len(y) - 1:
                print(" | ", end="")
    print()


