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

n = int(input("Finding HCF and LCM of how many numbers?"))
print("Number should be greater than 0.")
number = int(input("Enter your first number: "))

hcf = factor(number)
lcm = factor(number)

if n > 2:
    for i in range(0,n-2):
        number = int(input("Next number: "))
        highcf(number)
        leastcm(number)

lastNumber = int(input("Enter last number: "))
highcf(lastNumber)
leastcm(lastNumber)

print("HCF is ", math.prod(hcf))
print("LCM is ", math.prod(lcm))