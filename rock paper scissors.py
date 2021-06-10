import random

choices = ['rock','paper','scissors']

print('rock = 0')
print('paper = 1')
print('scissors = 2')
choice = int(input('What do you choose: '))

user_choice = choices[choice]
computer_choice = random.choice(choices)


if user_choice == 'rock' and computer_choice == 'paper':
    print('You loose! You choose',user_choice,'and the computer choose',computer_choice)
elif user_choice == 'rock'and computer_choice == 'scissors':
    print('You Win! You choose',user_choice,'and the computer choose',computer_choice)
elif user_choice == 'rock' and computer_choice == 'rock':
    print("It's a TIE! You choose",user_choice,"and the computer choose",computer_choice)
    

if user_choice == 'paper' and computer_choice == 'rock':
    print('You Win! You choose',user_choice,'and the computer choose',computer_choice)
elif user_choice == 'paper'and computer_choice == 'paper':
    print("It's a TIE! You choose",user_choice,"and the computer choose",computer_choice)
    
elif user_choice == 'paper'and computer_choice == 'scissors':
    print('You loose! You choose',user_choice,'and the computer choose',computer_choice)

if user_choice == 'scissors' and computer_choice == 'rock':
    print('You loose! You choose',user_choice,'and the computer choose',computer_choice)   
elif user_choice == 'scissors'and computer_choice == 'paper':
    print('You Win! You choose',user_choice,'and the computer choose',computer_choice)
elif user_choice == 'scissors'and computer_choice == 'scissors':
    print("It's a TIE! You choose",user_choice,"and the computer choose",computer_choice)
    
