numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
    if i == 1:
        primes.remove(i)

print(primes)
print(not_primes)