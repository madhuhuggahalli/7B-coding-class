import random
import matplotlib
import matplotlib.pyplot as plt


def play_game():
    roll = random.randint(1,100)
    if roll == 100:
        return False # you lose
    elif roll <= 50:
        return False # you lose
    elif 100 > roll >= 50:
        return True # you win


#define the gambler function
def simple_gambler(funds,initial_bet,bet_count):
    broke_count = 0
    value = funds
    bet = initial_bet
    wX = []    # wager X
    vY = []    #value Y

    # change to 1, to avoid confusion so we start @ wager 1
    # instead of wager 0 and end at 100.
    currentBet = 1

    while currentBet <= bet_count:
        if play_game():
            value += bet
            # append #
            wX.append(currentBet)
            vY.append(value)

        else:
            value -= bet
            # append #
            wX.append(currentBet)
            vY.append(value)

        currentBet += 1

        if value<0: broke_count +=1

    plt.plot(wX,vY)
    return broke_count


x = 0
# start this off @ 1, then add, and increase 50 to 500, then 1000
broke = 0.0
totalruns = 100
while x < totalruns:
    a = simple_gambler(10000,100,10000)
    x += 1
    if a>0: broke += 1.0
bankruptcy_rate = 100*broke/totalruns
print ("the bankruptcy rate is %f percent" %bankruptcy_rate)
plt.ylabel('Account Value')
plt.xlabel('Bet Count')
plt.show()

# https://pythonprogramming.net/plotting-monte-carlo-matplotlib/?completed=/simple-bettor/
