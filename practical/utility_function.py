"""
Q.
Practical Exercises (2 hours)
- Create utility functions for data manipulation
Build a simple command-line tool
- Practice error handling scenarios |
"""
# Game
# Dice Game
import random

def make_wishes():
    print("Makes wishes and mention your life's asperiation: ")
    aspiration = input()
    
    print("Make any amount of offering (Nyndhar): ")
    nynder = input()

    print("Press any key to roll your three dice. ")
    input()
    print("Your Aspiration is to:", aspiration, "and you have offer Nu.", nynder, "as a Nyndhar")

def roll():
    num1, num2, num3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    total_roll = num1 + num2 + num3
    print("Your dice roll number are: ", num1, num2, num3)
    print("Your total dice roll is: ", total_roll)

    if total_roll ==12:
        print("Today is your bad day.  Chill and relex in your room plz!")
    elif total_roll % 2 == 0:
        print("This is your lucky day. You will achieve your dream.")
    else: 
        print("The luck is not favourable for you today.")

make_wishes()
roll()
    