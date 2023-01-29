# In a game, the player tosses two coins.
# Let’s suppose that, if the first and second coin land on heads, the player wins $10;
# if the first lands on heads and the second on tails, the player wins $5;
# otherwise, the player loses.
# We want a program that reads the value of the two coins (heads or tails) and determines whether the player has won.
# If yes, it should display the amount won.
import random
i = 0
wins = 0
while i <2:
    coin = random.randint(0,1)
    if coin == 0:
        coinStatus = "heads"
    else:
        coinStatus = "tails"
    print("Coin landed on " + coinStatus)
# 0 - heads
# 1 - tails
    if coin == 1:
        wins +=1
    i = i+1

print("You won " + str(wins * 5) + "$")
