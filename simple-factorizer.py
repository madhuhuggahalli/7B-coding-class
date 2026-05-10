def factorize(n):
    counter = 0
    for x in range(2, n):
        if n % x == 0:
            print x, 'is a factor'
            counter += 1
    if counter == 0:
            print n, 'is a prime number'

xx = int(input("Enter a number: "))
factorize(xx)
