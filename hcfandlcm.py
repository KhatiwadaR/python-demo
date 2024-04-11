import math

primeNum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def factor(num):
    factor = []
    for item in primeNum:
        while num%item == 0:
            factor.append(item)
            num = num/item
            if num == 1:
                break
    factor.append(int(num))
    return factor

def highcf(num):
    for item in hcf:
        if num % item == 0:
            num = num/item
        else:
            hcf.remove(item)
    
def leastcm(num):
    global lcm
    for item in lcm:
        if num % item == 0:
            num = num/item
            if num == 1:
                break

    if int(num) != 1:
        lcm.extend(factor(num))

while True:
        try:
            n = int(input("Finding HCF and LCM of how many numbers?\n"))
            num = int(input("Enter first number : "))
            1/n + 1
            1/num + 1

        except:
            print('Please Enter real number.')
        
        else:
            break

hcf = factor(num)
lcm = factor(num)

def number():
    while True:
        try:
            num = int(input("Enter your number: "))
            1/num + 1
           
        except:
            print('Please Enter real number.')
        
        else:
            break

    highcf(num)
    leastcm(num)

if n > 1:
    for i in range(1,n):
        number()


print("HCF is ", math.prod(hcf))
print("LCM is ", math.prod(lcm))
