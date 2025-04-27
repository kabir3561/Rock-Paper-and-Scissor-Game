import random

def Game():
    print('You want to play rock, paper, scissor game?')
    Consent = input('Enter your opinion: ').lower()

    if Consent == 'yes':
            while(True):
                user_choice = int(input('Choose your unmber: [0 = Rock, 1 = Paper, 2 = Scissor]'))
                
                computer_choice = random.randint(0, 2)
                if user_choice >= 3 or user_choice < 0:
                        print('You choose a wrong number')
                        break

                if computer_choice == user_choice:
                    print('Game is draw')
                elif computer_choice == 2 and user_choice == 0:
                    print('You Win!!')
                elif computer_choice == 0 and user_choice == 2:
                    print('Compuer Win!!')
                elif computer_choice > user_choice:
                    print('Compuer Win!!')
                elif computer_choice < user_choice:
                    print('You Win!!')
                
                print(f'Your choice is {user_choice} and Syster choices {computer_choice}')


    else:
        print('User don\'t want to play game.' )


Game()


