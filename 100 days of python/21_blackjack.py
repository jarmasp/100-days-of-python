import random

def draw():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def blackjack():
    print('Welcome to Blackjack!')
    print('The goal is to get as close to 21 as possible without going over.')
    print('Dealer hits until she reaches 17. Aces count as 1 or 11.')
    print('')

    player = []
    dealer = []
    player.append(draw())
    dealer.append(draw())
    player.append(draw())
    dealer.append(draw())

    print('Your cards: ', player, 'Current score: ', sum(player))
    print('Dealer\'s first card: ', dealer[0])

    while True:
        choice = input('Type \'y\' to get another card, type \'n\' to pass: ')
        if choice == 'y':
            player.append(draw())
            print('Your cards: ', player, 'Current score: ', sum(player))
            print('Dealer\'s first card: ', dealer[0])
            if sum(player) > 21 and 11 in player:
                player[player.index(11)] = 1
                print('Your cards: ', player, 'Current score: ', sum(player))
                print('Dealer\'s first card: ', dealer[0])
        else:
            break

    if sum(player) > 21:
        print('You went over. You lose.')
    elif sum(player) == 21:
        print('You win!')
    elif sum(dealer) == 21:
        print('Dealer wins!')
    elif sum(dealer) == 21 and sum(player) == 21:
        print('Draw.')
    else:
        while sum(dealer) < 17:
            dealer.append(draw())
        print('Dealer\'s cards: ', dealer, 'Dealer\'s score: ', sum(dealer))
        if sum(dealer) > 21:
            print('Dealer went over. You win.')
        elif sum(player) > sum(dealer):
            print('You win.')
        elif sum(player) < sum(dealer):
            print('You lose.')
        else:
            print('Draw.')

blackjack()