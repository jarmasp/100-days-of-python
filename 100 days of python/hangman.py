import random as r

wordList = ["python", "java", "kotlin", "javascript"]

def hangman(wordList):
    word = r.choice(wordList)
    print (word)

    display = []
    for i in word:
        display += "_"

    print (''.join(display))

    lives = 6
    end_game = False

    while not end_game:
        guess = input('guess a letter: ').lower()
        if len(guess) > 1:
            print('You should input a single letter')
        elif guess not in word:
            lives -= 1
            print ('you have ' + str(lives) + 'tries left')
            print('wrong')
            if lives == 0:
                print('You lose')
                end_game = True
        else:
            for position in range(len(word)):
                letter = word[position]
                if letter == guess:
                    print('right')
                    display[position] = letter
        print (''.join(display))
        if '_' not in display:
            end_game = True
            print ('You win!')