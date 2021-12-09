a = ' An apple a day keeps the doctor away'
a = a.lower()
print (a)
z = {}
for i in a:
    z[f'{i}'] =a.count(i)
print(z)