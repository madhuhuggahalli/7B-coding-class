def sieve(n):
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime

a = int(input("up to which number do you want to search? "))
result = sieve(a)
print max(result)
for ans in result:
    print ans

