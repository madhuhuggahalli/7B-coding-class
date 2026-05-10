tuple1 = ('tom', 'jerry', 2016, 2015)
tuple2 = (1, 2, 3, 4, 5 )
tuple3 = "a", "b", "c", "d"

print tuple1

tuple4 = ()
tuple5 = (50,)
print tuple5

print len(tuple1)

tuple9 = tuple1 + tuple2
print tuple9

a = 4 in tuple2
print a

for x in tuple3:
    print x


print (cmp(tuple3, tuple2))


a = (1, 2, 3, 4, 5)
b = [6, 7, 7, 9, 10]
c = zip(a, b)
print c
results = [0]*len(a)
print results

a = 5
b = 2
print divmod(a, b)
print a%b
