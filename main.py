import random
def perevod(y):
    J_0 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
    return(J_0[y])

def perevod_out(y):
    J_0 = {'A': 0, 'B': 1, 'C': 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    return J_0[y]



def kp(paluba):
    #print(paluba)
    j_gor = random.randint(1, 2) #горизонтальное или вертикальное смещение
    j_x_x = random.randint(0, paluba) #СДВИГ ПАЛУБЫ
    j_x_x_x = random.randint(1, 2) # в какую сторону сдвигаем
    if j_gor == 1:
        j_x = random.randint(0 + paluba, 10 - paluba)
        if j_x_x_x == 1:
            j_y = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{j_x}{j_y},{j_x}{j_y}')
        else:
            j_y = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{j_x}{j_y},{j_x}{j_y}')
    else:
        j_y = random.randint(0 + paluba, 10 - paluba)
        j_y_y_y = random.randint(1, 2)
        if j_y_y_y == 1:
            j_x = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{j_x}{j_y},{j_x}{j_y}')
        else:
            j_x = random.randint(0 + paluba, 10 - paluba)
            temp = (f'{j_x}{j_y},{j_x}{j_y}')
    return(temp)


#def R_C(pleer):

#rast = ('E6_A6','E6_A6','F5_F9')
k4=kp(4)
#print(zanat_kv(k4))
#print(k4)
#prover_rast(rast)
    #k3 = pass
    #k2 = pass
    #k1 = pass