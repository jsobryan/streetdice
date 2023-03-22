import random
from dataclasses import dataclass
from time import sleep


###will eventually add logic that will have 'other players' make random bets against the player
@dataclass
class Otherplayers:
    bet: random.randint(10,50)
    bankroll: int

@dataclass
class Player:
    playerbank: int

def gameloop():
    p1 = Player(50)
    win = [7,11]
    lose = [2, 3, 12, point]
    d1 = random.randint(1,7)
    d2 = random.randint(1,7)
    dtotal = d1 + d2
    pot = 0
    
    while True:
        
        def rollagain():
            while True:
                rollagain = input("Roll Again (Y/N): ")
                if rollagain.lower() not in ("y","n"):
                    continue
                else:
                    break
        def checkroll(user_input, list_to_check):
            if user_input in list_to_check:
                return True
            else:
                return False
        def printbank():
            print(f'Your current bankroll: {p1.playerbank}\n\n')
        def playerbet():
            while True:
                playerbet = int(input("Your Bet: "))
                if playerbet <0:
                    print('You cannot bet less than zero')
                    continue
                elif playerbet > p1.playerbank:
                    print('You cannot bet more than you have')
                    continue
                else:
                    return playerbet
        def rolldie():
            printbank()
            point = 0
            num_rolls = 1
            d1 = random.randint(1,7)
            d2 = random.randint(1,7)
            dtotal = d1 + d2
            bet = playerbet()
            print(f'Player rolls a {d1} and a {d2} for a total of {dtotal}')
            ###This should check if the roll is a win or a loss, and if neither, the total becomes the new 'point' provided it is the first roll after a win or loss.  After the point is set, player will lose if it is rolled before 7 or 11.  subsequent bets will be added to the 'pot' until a win or loss
            if checkroll(dtotal,win):
                print("You Win!\n")
                p1.playerbank += bet
                p1.playerbank += pot
                printbank()
                num_rolls = 0
            elif checkroll(dtotal,lose):
                print("You Lose!\n")
                p1.playerbank -= bet
                printbank()
                num_rolls = 0
            elif num_rolls == 1:
                point = dtotal
                print(f'The point is now {point}\n')
                num_rolls = 0
                pot += bet
        rolldie()

if __name__ == "__main__":
    gameloop()

