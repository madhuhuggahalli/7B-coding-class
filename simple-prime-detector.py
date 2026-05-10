#this is the function to test whether a number is prime or not
def factorize(n):
    counter = 0
    for x in range(2, n):
        if n % x == 0:
            counter += 1
    if counter == 0:
        print("    %d is prime" % (n))

#this is the function that looks through all numbers, testing each one
def primesearch(pri):
        for y in range(2, pri):
            factorize(y)
maxe = int(input("Enter the number you want to search up to: "))
primesearch(maxe)
