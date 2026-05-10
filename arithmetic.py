import time
import random
import os

starttime = time.time()
elapsedtime = time.time() - starttime

sleep = 5
timelimit = 10
score = 0


while elapsedtime <= timelimit:
    elapsedtime = time.time() - starttime
    digits = list(range(1, 10, 1))
    operators = list(range(1, 4, 1))

    first = random.choice(digits)
    second = random.choice(digits)
    operator = random.choice(operators)

    if operator == 1:
        result = first+second
        marker = "+"
    elif operator == 2:
        result = first-second
        marker = '-'
    elif operator == 3:
        result = first*second
        marker = '*'

    timekeeper = time.time()

    print first, marker, second
    response = int(input("whats the answer? "))

    if (time.time() - timekeeper) <= sleep:
        if response == result:
            print("correct " )
            score += 1
        elif response != result:
            print ("wrong " )
    elif (time.time() - timekeeper) > sleep:
        print ("too late")
        print ("you took "), (time.time() - timekeeper), ("seconds")

print ("time's up")
os.system(("say 'your time is up'"))
print ("your score is "), score
