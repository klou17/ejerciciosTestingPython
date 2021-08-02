import math

def isPrime(number):
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):  
        if (number%check) == 0:  
            return False
    return True


def check(n):
    print ("isPrime(" +str(n) +")= "+ str(isPrime(n)))


check(9)
check(15)
check(25)
check(49)

