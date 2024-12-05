import random

emojis = {'r':'🪨', 'p':'📰', 's':'✂️'}
choices = ('r', 'p', 's')

while True:
    user_choices = input('Rock (r)🪨, Paper (p)📰, Scissors (s)✂️ ? :').lower()
    if user_choices not in choices:
        print('Invalid choice!')
        continue


    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choices]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choices == computer_choice:
        print('Tie!')
    elif( (user_choices == 'r' and computer_choice == 's') 
         or (user_choices == 'p' and computer_choice == 'r') 
         or (user_choices == 's' and computer_choice == 'p')):
        print('You won 🎉🎆🎉')
    else:
        print('You lose 😞')
    should_continue = input('Continue?(y/n)> ').lower()
    if should_continue == 'n':
        break
