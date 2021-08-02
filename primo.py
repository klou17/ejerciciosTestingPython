import math
def isPrime(number):
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number))+1):  
        if (number%check) == 0:  
            return False
    return True

def test():
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(9) == False
    assert isPrime2(23) == True
    assert isPrime2(25) == False
    assert isPrime2(49) == False


test()