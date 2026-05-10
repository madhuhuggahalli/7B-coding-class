#values of possible coins, in descending order
units = (500, 100, 25,10,5,1)

#doing this and not appends to make tuple unpacking work
results = [0]*len(units)

#use raw_input for python2
initial_change = int(input('Change to make: '))
remaining_change = initial_change

for index, coin in enumerate(units):
    results[index], remaining_change = divmod(remaining_change, coin)
print("In order to make change for %d cents:" % initial_change)
for amount, coin in zip(results, units):
    print("    %d %d cent unit(s)" % (amount, coin))
