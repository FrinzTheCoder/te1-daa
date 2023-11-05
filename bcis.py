import random
import time

# generating dataset if not exist
try:
    with open('tc1_500_a.txt') as f:
        tc1_500_a = f.readline()
    tc1_500_a = tc1_500_a.split(',')
    for i in range(0,len(tc1_500_a)):
        tc1_500_a[i] = int(tc1_500_a[i])
    
    with open('tc2_500_d.txt') as f:
        tc2_500_d = f.readline()
    tc2_500_d = tc2_500_d.split(',')
    for i in range(0,len(tc2_500_d)):
        tc2_500_d[i] = int(tc2_500_d[i])
    
    with open('tc3_500_r.txt') as f:
        tc3_500_r = f.readline()
    tc3_500_r = tc3_500_r.split(',')
    for i in range(0,len(tc3_500_r)):
        tc3_500_r[i] = int(tc3_500_r[i])
    


    with open('tc4_5000_a.txt') as f:
        tc4_5000_a = f.readline()
    tc4_5000_a = tc4_5000_a.split(',')
    for i in range(0,len(tc4_5000_a)):
        tc4_5000_a[i] = int(tc4_5000_a[i])
    
    with open('tc5_5000_d.txt') as f:
        tc5_5000_d = f.readline()
    tc5_5000_d = tc5_5000_d.split(',')
    for i in range(0,len(tc5_5000_d)):
        tc5_5000_d[i] = int(tc5_5000_d[i])
    
    with open('tc6_5000_r.txt') as f:
        tc6_5000_r = f.readline()
    tc6_5000_r = tc6_5000_r.split(',')
    for i in range(0,len(tc6_5000_r)):
        tc6_5000_r[i] = int(tc6_5000_r[i])



    with open('tc7_50000_a.txt') as f:
        tc7_50000_a = f.readline()
    tc7_50000_a = tc7_50000_a.split(',')
    for i in range(0,len(tc7_50000_a)):
        tc7_50000_a[i] = int(tc7_50000_a[i])
    
    with open('tc8_50000_d.txt') as f:
        tc8_50000_d = f.readline()
    tc8_50000_d = tc8_50000_d.split(',')
    for i in range(0,len(tc8_50000_d)):
        tc8_50000_d[i] = int(tc8_50000_d[i])
    
    with open('tc9_50000_r.txt') as f:
        tc9_50000_r = f.readline()
    tc9_50000_r = tc9_50000_r.split(',')
    for i in range(0,len(tc9_50000_r)):
        tc9_50000_r[i] = int(tc9_50000_r[i])

except:
    tc1_500_a = [i for i in range(500)]
    temp = ""
    for chr in tc1_500_a:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc1_500_a.txt', 'w') as f:
        f.write(temp)

    tc2_500_d = [i for i in range(500,0,-1)]
    temp = ""
    for chr in tc2_500_d:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc2_500_d.txt', 'w') as f:
        f.write(temp)

    tc3_500_r = []
    for i in range(500):
        tc3_500_r.append(random.randrange(500))
    temp = ""
    for chr in tc3_500_r:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc3_500_r.txt', 'w') as f:
        f.write(temp)



    tc4_5000_a = [i for i in range(5000)]
    temp = ""
    for chr in tc4_5000_a:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc4_5000_a.txt', 'w') as f:
        f.write(temp)

    tc5_5000_d = [i for i in range(5000,0,-1)]
    temp = ""
    for chr in tc5_5000_d:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc5_5000_d.txt', 'w') as f:
        f.write(temp)

    tc6_5000_r = []
    for i in range(5000):
        tc6_5000_r.append(random.randrange(5000))
    temp = ""
    for chr in tc6_5000_r:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc6_5000_r.txt', 'w') as f:
        f.write(temp)



    tc7_50000_a = [i for i in range(50000)]
    temp = ""
    for chr in tc7_50000_a:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc7_50000_a.txt', 'w') as f:
        f.write(temp)

    tc8_50000_d = [i for i in range(50000,0,-1)]
    temp = ""
    for chr in tc8_50000_d:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc8_50000_d.txt', 'w') as f:
        f.write(temp)

    tc9_50000_r = []
    for i in range(50000):
        tc9_50000_r.append(random.randrange(50000))
    temp = ""
    for chr in tc9_50000_r:
        temp += str(chr)+','
    temp = temp[:len(temp)-1]
    with open('tc9_50000_r.txt', 'w') as f:
        f.write(temp)


def ISEQUAL(array, SL, SR):
    for k in range(SL + 1, SR):
        if array[k] != array[SL]:
            array[k], array[SL] = array[SL], array[k]
            return k
    return -1

def InsRight(array, CurrItem, SR, right):
    j = SR
    while j <= right and CurrItem > array[j]:
        array[j - 1] = array[j]
        j += 1
    array[j - 1] = CurrItem

def InsLeft(array, CurrItem, SL, left):
    j = SL
    while j >= left and CurrItem < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = CurrItem

def SWAP(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bcis(array):
    SL = 0
    SR = len(array) - 1

    while SL < SR:
        # SWAP(array, SR, SL + int((SR-SL)/2))
        if array[SL] == array[SR]:
            check = ISEQUAL(array, SL, SR)
            if check == -1:
                return array
        if array[SL] > array[SR]:
            SWAP(array, SL, SR)
        # if SR - SL >= 100:
        #     for i in range(SL + 1, (SR-SL)^0.5):
        #         if array[SR] < array[i]:
        #             SWAP(array, SR, i)
        #         elif array[SL] > array[i]:
        #             SWAP(array, SL, i)
        # else:
        i = SL + 1
        LC = array[SL]
        RC = array[SR]
        while i < SR:
            CurrItem = array[i]
            if CurrItem >= RC:
                array[i] = array[SR - 1]
                InsRight(array, CurrItem, SR, len(array)-1)
                SR -= 1
            elif CurrItem <= LC:
                array[i] = array[SL + 1]
                InsLeft(array, CurrItem, SL, 0)
                SL += 1
                i += 1
            else:
                i += 1
        SL += 1
        SR -= 1
    return array

temp = time.time()
bcis(tc1_500_a)
temp2 = time.time()

print("Waktu untuk TC1 (500, sorted):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc2_500_d)
temp2 = time.time()

print("Waktu untuk TC2 (500, reversed):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc3_500_r)
temp2 = time.time()

print("Waktu untuk TC3 (500, random):",str(temp2-temp),"detik")



temp = time.time()
bcis(tc4_5000_a)
temp2 = time.time()

print("Waktu untuk TC4 (5000, sorted):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc5_5000_d)
temp2 = time.time()

print("Waktu untuk TC5 (5000, reversed):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc6_5000_r)
temp2 = time.time()

print("Waktu untuk TC6 (5000, random):",str(temp2-temp),"detik")


temp = time.time()
bcis(tc7_50000_a)
temp2 = time.time()

print("Waktu untuk TC7 (50000, sorted):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc8_50000_d)
temp2 = time.time()

print("Waktu untuk TC8 (50000, reversed):",str(temp2-temp),"detik")

temp = time.time()
bcis(tc9_50000_r)
temp2 = time.time()

print("Waktu untuk TC9 (50000, random):",str(temp2-temp),"detik")