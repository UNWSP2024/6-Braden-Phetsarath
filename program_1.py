
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

#Braden Phetsarath
#10/6
#100 2dice average
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    import random
    r1 = (random.randint(1, 6))
    r2 = (random.randint(1, 6))
    # Sum 2 numbers
    # return sum to calling function
    return r1 + r2
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total = 0
    count = 100
    for i in range(100):
        value = randDice()
        total += value
    average = total / count
    print (f"average result: {average:.2f}")


if __name__ == "__main__":
    main()

