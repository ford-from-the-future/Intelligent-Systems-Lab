# The purpose of this assignment is the application of queues.

# A prime number is a positive integer other than 1 and is divisible only by 1 and itself.
# For example, 7 is a prime number because the only positive factors of 7 are 1 and 7.
# On the other hand, 12 is not a prime number because 2, 3, 4, and 6 are also factors of 12.

# You are asked to write a function to compute the prime numbers up to a given value.
# The function is named sieve, and it will take an integer value as parameter.
# The function should return a list that contains all prime numbers up to (and including, if appropriate)
# value, the numbers in the returned list must be in ascending order.

from array_queue import ArrayQueue

def sieve(numberValue):

    primes = [True for _ in range(numberValue + 2)] #Set TRUE condition for what a Prime actually is

    p = 2 #Assign p to int 2 for evaluation later

    while p * p <= numberValue: #While loop to confirm prime less than provided value (numberValue)

        if primes[p]: #Checks to see if p has not been changed, if so, then it is a Prime

            for i in range(p * 2, numberValue + 2, p): #Update all multiples of value stored in P variable

                primes[i] = False
        p += 1

    return [i for i in range(2, numberValue + 1) if primes[i] == True] #Finally, returns the list of primes