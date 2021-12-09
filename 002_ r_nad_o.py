a =[1, 1, 1, 1, 1,1]
couples = dict.formkeys(set(a), 0)

for i in enumerate(a):
    for j in a[i[0]+1:]:
        if j == i[1]:
            couples[i[1]]+=1

    for key, value in dict.items():
        if value != 0:
            print(f'{key} - {value} пар')