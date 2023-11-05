# source: 
# https://www.geeksforgeeks.org/counting-sort/

# generating dataset if not exists
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




def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)
 
    # Initializing count_array with 0
    count_array = [0] * (M + 1)
 
    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1
 
    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array

temp = time.time()
count_sort(tc1_500_a)
temp2 = time.time()

print("Waktu untuk TC1 (500, sorted):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc2_500_d)
temp2 = time.time()

print("Waktu untuk TC2 (500, reversed):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc3_500_r)
temp2 = time.time()

print("Waktu untuk TC3 (500, random):",str(temp2-temp),"detik")



temp = time.time()
count_sort(tc4_5000_a)
temp2 = time.time()

print("Waktu untuk TC4 (5000, sorted):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc5_5000_d)
temp2 = time.time()

print("Waktu untuk TC5 (5000, reversed):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc6_5000_r)
temp2 = time.time()

print("Waktu untuk TC6 (5000, random):",str(temp2-temp),"detik")


temp = time.time()
count_sort(tc7_50000_a)
temp2 = time.time()

print("Waktu untuk TC7 (50000, sorted):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc8_50000_d)
temp2 = time.time()

print("Waktu untuk TC8 (50000, reversed):",str(temp2-temp),"detik")

temp = time.time()
count_sort(tc9_50000_r)
temp2 = time.time()

print("Waktu untuk TC9 (50000, random):",str(temp2-temp),"detik")