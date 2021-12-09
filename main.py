import random
def perevod(y):
    J_0 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
    return(J_0[y])

def perevod_out(y):
    J_0 = {'A': 1, 'B': 2, 'C': 3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10}
    return J_0[y]

def zanat_kv(a):
    zanjal = set()
    b = a[0:1]
    c = a[(a.index('_')+1):(a.index('_')+2)]
    d = int(a[1:(a.index('_'))]) #цифра 1
    e = int(a[(a.index('_')+2)]) #цифра 2



def kp(paluba):
    print(paluba)
    j_gor = random.randint(1, 2) #горизонтальное или вертикальное смещение
    j_x_x = random.randint(0, paluba) #СДВИГ ПАЛУБЫ
    j_x_x_x = random.randint(1, 2) # в какую сторону сдвигаем
    if j_gor == 1:
        j_x = random.randint(0 + paluba, 10 - paluba)
        if j_x_x_x == 1:
            j_y = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{perevod(j_x - paluba + 1)}{j_y}_{perevod(j_x)}{j_y}')
        else:
            j_y = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{perevod(j_x)}{j_y}_{perevod(j_x + paluba-1)}{j_y}')
    else:
        j_y = random.randint(0 + paluba, 10 - paluba)
        j_y_y_y = random.randint(1, 2)
        if j_y_y_y == 1:
            j_x = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{perevod(j_x)}{j_y - paluba+1}_{perevod(j_x)}{j_y}')
        else:
            j_x = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{perevod(j_x)}{j_y}_{perevod(j_x)}{j_y + paluba-1}')

    return(temp)

#def R_C(pleer):

rast = ('E6_A6','E6_A6','F5_F9')
k4=kp(1)
print(zanat_kv(k4))
print(k4)
#prover_rast(rast)
    #k3 = pass
    #k2 = pass
    #k1 = pass