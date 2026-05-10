import random
import matplotlib
import matplotlib.pyplot as plt


def play_game():
    wheel = (1,2,3,4,5,6,7,8,9,0)
    wheel1 = random.choice(wheel)
    wheel2 = random.choice(wheel)
    wheel3 = random.choice(wheel)
    if ((wheel1 == wheel2) and (wheel2 == wheel3)) and (wheel1 == 0):
        jackpot = 2
    elif ((wheel1 == wheel2) and (wheel2 == wheel3)):
        jackpot = 1
    else:
        jackpot = 0
    return jackpot



#define the gambler function
def simple_gambler(funds,initial_bet,bet_count):
    broke_count = 0
    value = funds
    bet = initial_bet
    wX = []    # wager X
    vY = []    #value Y
    currentBet = 1

    while currentBet <= bet_count:
        outcome = play_game()

        if (outcome == 2):
            value += bet*500
            # append #
            wX.append(currentBet)
            vY.append(value)
        elif (outcome == 1):
            value += bet*10
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
broke = 0.0
totalruns = 800
while x < totalruns:
    a = simple_gambler(10000,100,5000)
    x += 1
    if a>0: broke += 1.0
bankruptcy_rate = 100*broke/totalruns
print ("the bankruptcy rate is %f percent" %bankruptcy_rate)
plt.ylabel('Account Value')
plt.xlabel('Bet Count')
plt.show()


