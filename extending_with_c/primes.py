from time import perf_counter
from math import isqrt
from typing import List
import prime_shared
def prime(x: int)-> int:
    """check if x is prime O(sqrt(n)) time complexity
    """
    
    if x <= 1:
        x = prime(int(input("Enter another integer > 1: ")))
        return x
    
    elif x == 2:
        print(f"True {x} is a prime number")
        return x
    
    else:
        i = 2
        while i <= isqrt(x):
            if x % i == 0:
                print(f"False {x} isnt a prime number")
                return x
            i += 1
    print(f"True {x} is a prime number")
    return x

def smaller_or_eq_primes(x: int) -> List[int]:
    """Find the prime numbers smaller or equal to x O[(n-2)sqrt(n)]"""
    prime_list: List[int] = [2]
    
    for j in range(3, x + 1):  # Iterating from 3 to x
        is_prime = True

        for i in range(2, isqrt(j) + 1):  # Check for divisors up to sqrt(j)
            if j % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(j)

    return prime_list

def get_x()->int:
    while True:
        try:
            x = int(input("Enter an integer > 1: ")) 
            if x <= 1:
                raise ValueError
        except TypeError:
            print("type error!") 
        except ValueError:
            print("Value error!")
        else:
            return x;

def main():
    # x = get_x()
    # start = perf_counter()
    # #prime_test = prime(x)
    # prime_list = smaller_or_eq_primes(x)
    # end = perf_counter()
    # print(f"Search time: {end-start:.7f}seconds")
    print(prime_shared.__doc__)
    print(prime_shared.__name__)
    
if __name__ == '__main__':
    main()