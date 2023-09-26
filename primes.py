"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("Inappropriate argument!")


    index = 1
    while True:
        index += 1
        flag = True
        for i in range(2, 1 + index // 2):
            if index % i == 0:
                flag = False
                break
                
        if flag:
            list.append(index)
            if len(list) >= number_of_primes:
                return list



primes(5)