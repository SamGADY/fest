rast = ['06_36', '46_66', '76_96', '75_78']

def zanat_kv(a):
    zanjal = set()
    temp = list()
    b = int(a[0:1]) #цифра 1 - x
    c = int(a[(a.index('_')+1):(a.index('_')+2)]) #цифра 1 - x
    d = int(a[1:(a.index('_'))]) #цифра 1 - y
    e = int(a[(a.index('_')+2)]) #цифра 2 - y
    if b == c:
        if d > e:
            while e <= d:
                temp.append([b, e])
                e += 1
        else:
            while d <= e:
                temp.append([b, d])
                d += 1
    else:
        if b > c:
            while c <= b:
                temp.append([c, d])
                c +=1
        else:
            while b <= c:
                temp.append([b, d])
                b += 1
    return(temp)

def zanat_pola(a = list):
    temp = []
    for i in a:
        print(type(a))
        z = -1
        while z <= 1:
            c = -1
            while c <=1:
                if (int(i[0])-z <0):
                    continue
                elif (int(i[0])-z >9):
                    continue
                elif (int(i[1])-c < 0):
                    continue
                elif (int(i[1])-c >9):
                    continue
                else:
                    temp.append([(int(i[0]) - z), (int(i[1]) - c)])
                c += 1
            z += 1
    return(temp)


for i in rast:
    temp = []
    temp_1 = []
    temp=(zanat_kv(i))


temp_1 = (zanat_pola(temp))

print(temp)
print(temp_1)

