import random
b = [random.randint(10, 20) for x in range(15)]
c = {}
for i in b:
    if i not in c.keys():
        c[i] = b.count(i)
    else:
        continue
for key, value in c.items():
    if value < 2:
        continue
    else:
        print(f'чисо {key} имеет {value-1} пары(у)')
