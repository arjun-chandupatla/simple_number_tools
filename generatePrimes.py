# iteratively generate list of primes less than a certain number

def sieve(num):
    primes = []
    numArray = range(2, num + 1)
    for i in numArray:
        try:
            isPrime = True
            for p in primes:
                if i < p^2:
                    break
                if i % p == 0:
                    isPrime = False
            if isPrime:
                primes.append(i)
        except IndexError:
            pass
    return primes
