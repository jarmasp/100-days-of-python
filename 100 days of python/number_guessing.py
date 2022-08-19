import random as r # Import the random module

hard = 5
easy = 10

def choose_dificulty():
    
    dificulty = input("Choose a dificulty. Type 'easy' or 'hard'. \n in easy you have 10 attemps, in hard you have 5 attemps ")
    if dificulty == 'easy':
        return easy 
    else:
        return hard

def check_answer(guess, number, attemps):
    print (f'you have {attemps} attemps')
    if guess > number:
        print ('Too high')
        return attemps - 1
    elif guess < number:
        print ('Too low')
        return attemps - 1
    else:
        print('You win!')
        play_again()

def play_again():
    play_again = input('Do you want to play again? Type "y" or "n": ')
    if play_again == 'y':
        number_guessing()
    else:
        print('Bye!')
        exit()

def number_guessing():

    number = r.randint(1, 100)

    print('welcome to number guessing game \n guess a number between 1 and 100')

    attemps = choose_dificulty()
    print (f'you have {attemps} attemps')

    while attemps > 0:
        guess = int(input('Guess a number: '))
        attemps = check_answer(guess, number, attemps)

    play_again()

number_guessing()