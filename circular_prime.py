"""
find circular prime in range 10^6
"""
from math import sqrt

def prime_check(n):
    if n <2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)+1)):
            if n % i == 0:
                return False
    return True

#only this digits are eligible (1, 3, 7, 9)
def circular_check(num):
    if not prime_check(num):
        return False
    i = str(num)
    while num > 0:
        if (num % 5 == 0) or (num % 2 == 0):
            return False
        num = num // 10
    circle = []
    for s in range(len(i)):
        w = i[s:] + i[:s]
        if prime_check(int(w)):
            circle.append(w)
        else:
            return False
    if len(circle) == len(i):
        return True

def circle_prime_nums(n):
    circle_num = set(i for i in range(n) if (circular_check(i)))
    return len(circle_num)+2 #add 2 -> for 2 and 5
            

if __name__ == "__main__":
    print(circle_prime_nums(1000000)) 

