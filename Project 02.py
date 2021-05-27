"""
Program Name: Project 02
Name: Christopher Borys
Date: 4/15/21

This Python project aims to emulate the popular casino game, Craps. Here are the rules:
    * Two six-sided dice are required to play and their total is collect at the end of each roll
    * If on the first roll the player rolls a 7 or an 11, the player automatically wins, and if
      the player should roll a 2, 3, or 12 on the first roll, then they shall automatically lose.
    * If the user rolls a 4, 5, 6, 8, 9, or 10 on the first roll, their total becomes the "point."
      The player will keep rolling the dice until they roll the point again, in which case they
      automatically win, roll a 7, in which case they automatically lose, or they walk from the
      table and stop playing.
    * While rolling the dice, the player is allowed to place wagers on:
            Rolling a total of: 4, 5, 6, 8, 9 , 10
                            or
            Rolling a double of: 2's (pays 7:1), 3's (pays 9:1), 4's (pays 9:1), or 5's (pays 7:1)

Here are the project guidelines:
    A. The program must begin the player with 100 coins to play with. Since the player can leave
       the game at any time, they will need to enter a sentinel value if they wish to leave. Once
       they decide to leave, the program will display how many coins they have.
                    **The player must put 5 coins on the PASS line to begin the game**
    B. The player must be allowed to place a bet before the game begins, either on the PASS line
       (a bet that the player will win) or the DON'T PASS line (a bet that the player will lose).
       The bet value will range from 1 to 5 coins.
    C. Once the first roll is finished and the point value is set, the program will allow the user
       to place a bet from 1 to 5 coins (if they still have coins) on whether or not the player
       will roll a specific number before they win or lose. The side-bet values they can bet on are
       the same as listed above in the game rules.
    D. If the player should win a side-bet, the total they win will be added to their total amount
       of coins, removing the coins from the board and increasing their overall balance.
            i.e., if the player bets 2 coins that they roll a 4 and they roll this 4 before they
            make point or roll a craps, the player shall receive 4 coins (their coins and the 2
            won from the bet)
    E. If the player rolls a craps (a 7) before the point is made, then all side-bets are lost and
       you must decrease their overall balance by the same amount as if they won.
"""

import random


class Roller:
    # This class handles the explicit dealings with rolling the dice

    def startMenu(self, coins):
        # This method displays a menu to the user asking if they want to start playing Craps.
        # Takes the number of coins as a parameter.
        menuFlag = True  # this Boolean flag runs the while loop below

        while menuFlag:  # runs as the flag is true
            print("Choose your option")
            print("------------------")
            print(" 1. Start playing")
            print(" 9. Quit")
            menuChoice = int(input("Enter option: "))

            if menuChoice == 1:  # executes if the user wants to play Craps
                menuFlag = False  # ends the loop
            elif menuChoice == 9:  # executes if the user wants to walk
                print("Thank you for playing Craps. You finished with", coins, "coins.")
                print("Aborting program...")
                quit()  # ends program
            else:  # executes if the user enters an invalid input
                print("Error: please enter valid input\n")

        return

    def firstRoll(self):
        # This method handles the first roll of the dice
        rollOne = random.randint(1, 7)  # first roll will be from 1 to 6, like an actual dice
        rollTwo = random.randint(1, 7)  # same as above, but stored as another roll
        totalRoll = rollOne + rollTwo  # stores the combined value of each roll

        if totalRoll == 7 or totalRoll == 11:  # executes if the combined roll value is either 7 or 11
            if totalRoll == 7:  # executes if combined roll is 7
                return totalRoll  # returns the 7
            else:  # executes if the combined roll is 11
                return totalRoll  # returns the 11
        elif totalRoll == 2 or totalRoll == 3 or totalRoll == 12:  # executes if the combined roll is 2, 3, or 12
            if totalRoll == 2:  # executes if the combined roll is a 2
                return totalRoll  # returns the 2
            elif totalRoll == 3:  # executes if the combined roll is a 3
                return totalRoll  # returns the 3
            else:  # executes if the combined roll is a 12
                return totalRoll  # returns the 12
        else:  # executes if the user rolls a value not explicitly listed above
            return totalRoll  # returns that value

    def rollCheck(self, coins):
        # This method handles asking the user if they want to keep rolling once the first roll is done.
        # Takes the user's number of coins as a parameter.
        continueRolling = True  # Boolean flag variable to control the while loop below
        while continueRolling:  # runs while flag is true
            print("Keep rolling?")
            print("-------------")
            print("\t1. Yes")
            print("\t2. No")
            choice = int(input("Enter choice: "))  # reads in user's choice

            if choice == 2:  # executes if user chose a 2, meaning they wish to stop rolling/playing
                print("Game ended. You finished with", coins, "coins.")  # prints the user's current coin value
                print("Thank you for playing Craps.")
                quit()  # ends program
            elif choice != 1 and choice != 2:  # executes if user makes an invalid choice
                print("Error: Please enter valid input.")
            else:
                return  # returns user's choice

    def singlesRoll(self):
        # This method runs if the user is rolling with an active single-valued side-bet.
        rollOne = random.randint(1, 7)  # stores first roll; just like the "roll" above in firstRoll()
        rollTwo = random.randint(1, 7)  # stores second roll
        rollTotal = rollOne + rollTwo  # stores combined value of the dice roll
        return rollTotal  # returns that combined value

    def doublesRoll(self, value):
        # This method runs if the user is rolling with an active doubles-valued side-bet.
        # Takes the value of the pair the user is betting on as a parameter.
        #       (i.e., if user is betting on rolling a pair of 3's, the method will read in a 3)
        rollOne = random.randint(1, 7)  # stores first roll
        rollTwo = random.randint(1, 7)  # stores second roll

        if rollOne == rollTwo and rollOne == value and rollTwo == value:  # executes if each dice roll matches parameter
            return rollOne  # returns value of that roll
        else:  # executes if rolls do not match
            print("Sorry, you did not roll a pair of doubles")
            return rollOne + rollTwo  # returns combined value of the two rolls

    def regularRoll(self):
        # This method runs if the user is rolling without an active side-bet.
        # This method is declared exactly the same as the singlesRoll() method above, but was created for code clarity
        # and knowing this method only runs if user does not have an active side-bet.
        rollOne = random.randint(1, 7)  # stores first roll
        rollTwo = random.randint(1, 7)  # stores second roll
        rollTotal = rollOne + rollTwo  # stores combined roll value
        return rollTotal  # returns that combined value


def beginningBetPrompt():
    # This method handles asking the user which betting line they want to bet on at the beginning of the game.
    promptFlag = True  # Boolean flag variable

    while promptFlag:  # runs while flag is true
        print("Choose which line to place beginning bet on")
        print("-------------------------------------------")
        print("\t1. PASS Line")
        print("\t2. DON'T PASS Line")
        lineChoice = int(input("\tEnter your choice: "))  # stores user's choice

        if lineChoice == 1:  # executes if user wants to bet on the PASS line; user input a 1 above
            return 1  # returns a 1
        elif lineChoice == 2:  # executes if user wants to bet on the DON'T PASS line; user input a 2 above
            return 2  # returns a 2
        else:  # executes if user input an invalid input
            print("Error: enter a valid input\n")


def passLine():
    # This method handles the case where the user chooses to bet on the PASS line
    betFlag = True  # Boolean flag variable

    while betFlag:  # runs while flag is true
        betValue = int(input("Enter value of bet (1 to 5 coins): "))  # stores user's bet wager
        if 1 <= betValue <= 5:  # executes if bet from 1 to 5
            return betValue  # returns wager
        else:  # executes if user placed an invalid input
            print("Error: please enter value input\n")


def dontPassLine():
    # This method handles the case where the user chooses to bet on the DON'T PASS line
    betFlag = True  # Boolean flag variable

    while betFlag:  # runs while flag is true
        betValue = int(input("Enter value of bet (1 to 5 coins): "))  # stores user's bet wager
        if 1 <= betValue <= 5:  # executes if bet from 1 to 5
            return betValue  # returns wager
        else:  # executes if user placed an invalid input
            print("Error: please enter value input\n")


def sidebetPrompt():
    # This method handles asking the user if they want to place a side-bet.
    sideFlag = True  # Boolean flag variable
    while sideFlag:  # runs while flag is true
        print("Would you like to place a side-bet?")
        print("\t1. Yes")
        print("\t2. No")
        choice = int(input("Enter your choice: "))  # stores user's choice

        if choice == 1:  # executes if the user chooses to place a side-bet; they input a 1
            return 1  # returns a 1
        elif choice == 2:  # executes if the user chooses not to place a side-bet; they input a 2
            return 2  # returns a 2
        else:  # executes if user placed an invalid input
            print("Error: please enter a valid input")


def sidebet():
    # This method handles asking the user the value of their side-bet and if it's a single value or pair of doubles
    sidebetFlag = True  # Boolean flag variable

    while sidebetFlag:  # runs while flag is true
        print("What you like to bet on rolling?")
        print("\t1. Single value")
        print("\t2. Doubles")
        sidebetChoice = int(input("Enter choice: "))  # stores user's choice of bet

        if sidebetChoice == 1:  # executes if the user chooses to roll for a single value; user input a 1
            print("Which value would you like to bet on rolling?")
            print("\t4\t5\t6\t8\t9\t10")
            singlesBet = int(input("Enter choice (the specific value): "))  # stores value of bet
            return singlesBet  # returns value
        elif sidebetChoice == 2:  # executes if user chooses to roll for a pair of doubles; user input a 2
            doublesFlag = True  # Boolean flag variable
            while doublesFlag:  # runs while flag is true
                print("Which value of doubles would you like to roll for?")
                print("\tPair of 2's (pays 7:1)")
                print("\tPair of 3's (pays 9:1)")
                print("\tPair of 4's (pays 9:1)")
                print("\tPair of 5's (pays 7:1)")
                doublesBet = int(input("Enter choice of doubles (the specific value): "))  # stores value of pair

                if 2 <= doublesBet <= 5:  # executes if user picks a value from 2 to 5
                    if doublesBet == 2:  # executes if the user chose to roll for a pair of 2's
                        return 92  # returns a 92 to represent the 2
                    elif doublesBet == 3:  # executes if the user chose to roll for a pair of 3's
                        return 93  # returns a 93 to represent the 3
                    elif doublesBet == 4:  # executes if the user chose to roll for a pair of 4's
                        return 94  # returns a 94 to represent the 4
                    elif doublesBet == 5:  # executes if the user chose to roll for a pair of 5's
                        return 95  # returns a 95 to represent the 5
                else:  # executes if user didn't choose a value from 2 to 5
                    print("Error: please enter valid pair of doubles")
        else:  # executes if the user's choice was an invalid input
            print("Error: please enter correct form of input")


def main():
    coins = int(100)  # initializes user's number of coins to be 100

    roller = Roller()  # creates class object
    roller.startMenu(coins)  # calls startMenu() and passes number of coins

    passLineBet = int(0)  # initializes the value of the PASS line bet to be 0
    dontPassLineBet = int(0)  # initializes the value of the DON'T PASS line bet to be 0
    betLine = beginningBetPrompt()  # stores value returned from method
    if betLine == 1:  # executes if user chose to bet on the PASS line
        passLineBet = passLine()  # stores value returned from method
    elif betLine == 2:  # executes if user chose to bet on the DON'T PASS line
        dontPassLineBet = dontPassLine()  # stores value returned from method

    point = int(0)  # initializes the point to be 0
    firstRoll = roller.firstRoll()  # stores value returned from method
    if firstRoll == 7 or firstRoll == 11:  # executes if user rolled a 7 or 11
        if betLine == 1:  # executes if the user originally placed bet on the PASS line
            coins += (passLineBet * 2)  # adds winnings to coin total
        elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
            coins -= (dontPassLineBet * 2)  # adds winnings to coin total
        print("Congratulations! You rolled a", firstRoll, "and won!")
        print("Final coin total:", coins, "\nThank you for playing Craps!")
        quit()  # ends program
    elif firstRoll == 2 or firstRoll == 3 or firstRoll == 12:  # executes if user rolled a 2, 3, or 12
        if betLine == 1:  # executes if the user originally placed bet on the PASS line
            coins -= (passLineBet * 2)  # subtracts losings from coin total
        elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
            coins += (dontPassLineBet * 2)  # adds winnings to coin total
        print("Sorry, you have rolled a", firstRoll, "and lost.")
        print("Final coin total:", coins, "\nThank you for playing Craps.")
        quit()  # ends program
    else:
        point = firstRoll  # value of roll is now made point
        print("You have rolled a", firstRoll)  # notifies user of their point value
        print(firstRoll, "is now the Point to match")
        print("Current coin total:", coins, "\n")

    roller.rollCheck(coins)  # calls method to see if user still wants to play

    mainFlag = True  # Boolean flag variable for the while loop below

    while mainFlag:  # runs while the flag is true
        sidebetChoice = sidebetPrompt()  # stores value returned from method
        wager = int(0)  # initializes wager to be 0
        doublesValue = int(0)  # initializes the pair value to be 0
        doublesRoll = int(0)  # initializes roll to be 0

        if sidebetChoice == 1:  # executes if user chose to roll for a single value
            sb = sidebet()  # stores value that user is rolling for
            if 4 <= sb <= 6 or 8 <= sb <= 10:  # executes if user is looking to roll a 4, 5, 6, 8, 9, or 10
                wager = int(input("Enter your side-bet wager (1 to 5 coins): "))  # stores the user's side-bet wager
                singlesRoll = roller.singlesRoll()  # stores what user rolled

                if singlesRoll == point:  # executes if the roll made the user's point
                    print("Congratulations! You made your point and have won!")

                    if singlesRoll == sb:  # executes if the user rolled their side-bet value
                        coins += (wager * 2)  # adds winnings to the coin total
                    elif singlesRoll != sb:  # executes if the user did not roll their side-bet value
                        coins -= (wager * 2)  # subtracts losings from coin total

                    if betLine == 1:  # executes if the user originally placed bet on the PASS line
                        coins += (passLineBet * 2)  # adds winnings to coin total
                    elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                        coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                    print("You finished with", coins, "coins.")
                    print("Thanks for playing Craps!")
                    quit()  # ends program
                elif singlesRoll == 7:  # executes if user rolled a 7
                    print("Sorry, you have rolled a 7 and have lost all side-bets by default.")
                    coins -= (wager * 2)  # subtracts losings from coin total
                    print("You currently have", coins, "coins")
                else:  # executes if roll was not point or a 7
                    print("You have rolled a", singlesRoll)
                    point = singlesRoll  # makes the roll the new point
                    print("Your point to match is now", point)  # notifies user of new point
                    print("Current coin total:", coins)
            elif 92 <= sb <= 95:  # executes if user wanted to roll for a pair of doubles
                wager = int(input("Enter your side-bet wager (1 to 5 coins): "))  # stores user's side-bet wager

                if sb == 92:  # executes if side-bet value passed was 92
                    doublesValue = 2  # adjusts value to 2
                elif sb == 93:  # executes if side-bet value passed was 93
                    doublesValue = 3  # adjusts value to 3
                elif sb == 94:  # executes if side-bet value passed was 94
                    doublesValue = 4  # adjusts value to 4
                elif sb == 95:  # executes if side-bet value passed was 95
                    doublesValue = 5  # adjusts value to 5

                if doublesValue > 1:  # executes if user's doubles side-bet value is higher than 1
                    doublesRoll = roller.doublesRoll(doublesValue)  # stores value of the roll
                    if doublesRoll == 2:  # executes if user rolled a pair of 2's
                        print("Congratulations! You rolled a pair of 2's. Payout is 7:1.")
                        coins += int(wager * 7)  # adds winnings to coin total (7:1 payout)
                        fullRoll = (doublesRoll * 2)  # then calculates the full roll; 2 + 2
                        if fullRoll == point:  # executes if full value of the roll is the point
                            print("Congratulations! You made your point and have won!")

                            if betLine == 1:  # executes if the user originally placed bet on the PASS line
                                coins += (passLineBet * 2)  # adds winnings to coin total
                            elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                                coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                            print("You finished with", coins, "coins.")
                            print("Thanks for playing Craps!")
                            quit()  # ends program
                        else:  # executes if full value of the roll was not the point
                            print("You have rolled a", fullRoll)
                            point = fullRoll  # this value is now the point
                            print("Your point to match is now", point)  # notifies user of new point
                            print("Current coin total:", coins)
                    elif doublesRoll == 3:  # executes if user rolls a pair of 3's
                        print("Congratulations! You rolled a pair of 3's. Payout is 9:1.")
                        coins += int(wager * 9)  # adds winnings to coin total (9:1 payout)
                        fullRoll = (doublesRoll * 2)  # then calculates the full roll; 3 + 3
                        if fullRoll == point:  # executes if full value of the roll is the point
                            print("Congratulations! You made your point and have won!")

                            if betLine == 1:  # executes if the user originally placed bet on the PASS line
                                coins += (passLineBet * 2)  # adds winnings to coin total
                            elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                                coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                            print("You finished with", coins, "coins.")
                            print("Thanks for playing Craps!")
                            quit()  # ends program
                        else:  # executes if full value of the roll was not the point
                            print("You have rolled a", fullRoll)
                            point = fullRoll  # this value is now the point
                            print("Your point to match is now", point)  # notifies user of new point
                            print("Current coin total:", coins)
                    elif doublesRoll == 4:  # executes if user rolls a pair of 4's
                        print("Congratulations! You rolled a pair of 4's. Payout is 9:1.")
                        coins += int(wager * 9)  # adds winnings to coin total (9:1 payout)
                        fullRoll = (doublesRoll * 2)  # then calculates the full roll; 4 + 4
                        if fullRoll == point:  # executes if full value of the roll is the point
                            print("Congratulations! You made your point and have won!")

                            if betLine == 1:  # executes if the user originally placed bet on the PASS line
                                coins += (passLineBet * 2)  # adds winnings to coin total
                            elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                                coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                            print("You finished with", coins, "coins.")
                            print("Thanks for playing Craps!")
                            quit()  # ends program
                        else:  # executes if full value of the roll was not the point
                            print("You have rolled a", fullRoll)
                            point = fullRoll  # this value is now the point
                            print("Your point to match is now", point)  # notifies user of new point
                            print("Current coin total:", coins)
                    elif doublesRoll == 5:  # executes if user rolls a pair of 5's
                        print("Congratulations! You rolled a pair of 5's. Payout is 7:1.")
                        coins += int(wager * 7)  # adds winnings to coin total (7:1 payout)
                        fullRoll = (doublesRoll * 2)  # then calculates the full roll; 5 + 5
                        if fullRoll == point:  # executes if full value of the roll is the point
                            print("Congratulations! You made your point and have won!")

                            if betLine == 1:  # executes if the user originally placed bet on the PASS line
                                coins += (passLineBet * 2)  # adds winnings to coin total
                            elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                                coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                            print("You finished with", coins, "coins.")
                            print("Thanks for playing Craps!")
                            quit()  # ends program
                        else:  # executes if full value of the roll was not the point
                            print("You have rolled a", fullRoll)
                            point = fullRoll  # this value is now the point
                            print("Your point to match is now", point)  # notifies user of new point
                            print("Current coin total:", coins)
                    elif doublesRoll == 7:  # executes if user rolls a 7
                        print("Sorry, you have rolled a 7 and have lost all side-bets by default.")
                        coins -= (wager * 2)  # user automatically loses side-bet; losings are subtracted from coins
                        print("You currently have", coins, "coins")
                    else:  # executes if user does not roll a pair of doubles or a 7
                        print("You have rolled a", doublesRoll)
                        point = doublesRoll  # this value is now the point
                        print("Your point to match is now", point)  # notifies user of new point
                        print("Current coin total:", coins)    
        elif sidebetChoice == 2:  # executes if user chose not to make a side-bet
            roll = roller.regularRoll()  # stores roll returned from method
            if roll == point:  # executes if roll was equal to the point
                print("Congratulations! You made your point and have won!")

                if betLine == 1:  # executes if the user originally placed bet on the PASS line
                    coins += (passLineBet * 2)  # adds winnings to coin total
                elif betLine == 2:  # executes if user originally placed bet on the DON'T PASS line
                    coins -= (dontPassLineBet * 2)  # subtracts losings from coin total

                print("You finished with", coins, "coins.")
                print("Thanks for playing Craps!")
                quit()  # ends program
            elif roll == 7:  # executes if the user rolls a 7
                print("You have rolled a Craps.")
                point = point  # point remains the same
                print("Your Point remains", point)  # reminds user of their point value
            else:  # executes if user does not make point or roll a 7
                print("You have rolled a", roll)
                point = roll  # rolled value now the point
                print("Your point to match is now", point)  # notifies user of new point
                print("Current coin total:", coins)

        roller.rollCheck(coins)  # asks user if they want to roll again


if __name__ == "__main__":
    main()
