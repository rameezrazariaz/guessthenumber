import random


def beginner():
    guesstime = 0
    n = random.randint(0, 10)
    print("Guess a number between 0 to 10\nYou have 5 tries")
    while guesstime < 5:
        guess = int(input("Take a guess: "))
        guesstime = guesstime + 1

        if guess < n:
            print("The guess is too low")
            # print(input("Guess again"))
            # guesstime=guesstime+1
        elif guess > n:
            print("The guess is too high")
            # print(input("Guess again"))
            # guesstime=guesstime+1
        elif guess == n:
            print("You have guessed the correct number")
            print("You took {} guesses".format(guesstime))
            break

    if guess != n:
        print("The number was {}".format(n))


def intermediate():
    guesstime = 0
    n = random.randint(0, 20)
    print("Guess a number between 0 to 20\nYou have 5 tries")
    while guesstime < 5:
        guess = int(input("Take a guess: "))
        guesstime = guesstime + 1

        if guess < n:
            print("The guess is too low")
        elif guess > n:
            print("The guess is too high")
        elif guess == n:
            print("You have guessed the correct number")
            print("You took {} guesses".format(guesstime))
            break

    if guess != n:
        print("The number was {}".format(n))


def advanced() -> object:
    guesstime = 0
    n = random.randint(0, 50)
    print("Guess a number between 0 to 50\nYou have 5 tries")
    while guesstime < 5:
        guess = int(input("Take a guess: "))
        guesstime = guesstime + 1

        if guess < n:
            print("The guess is too low")
        elif guess > n:
            print("The guess is too high")
        elif guess == n:
            print("You have guessed the correct number")
            print("You took {} guesses".format(guesstime))
            break

    if guess != n:
        print("The number was {}".format(n))


#def choice(i):
#    switcher = {
#        1: beginner(),
#        2: intermediate(),
#        3: advanced()
#    }
#    func = switcher.get(i, lambda: 'Invalid choice')
#    return func()


print("1 for beginner\n2 for intermediate\n3 for advanced")
i = input("Please select your choice: ")
#choice(i)

if i=='1':
    beginner()
elif i=='2':
    intermediate()
elif i=='3':
    advanced()
else:
    print("Invalid input")
