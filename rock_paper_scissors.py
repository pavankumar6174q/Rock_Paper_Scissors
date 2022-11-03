rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
images=[rock,paper,scissors]

user_choice=int(input("type 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice>=3 or user_choice<0:
    print("you have chosen wrong number so you loose")
else:
    print("you chose:")
    print(images[user_choice])

    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice==0 and user_choice==2:
        print("you loose")
    elif user_choice==computer_choice:
        print("its a draw")
    elif user_choice>computer_choice:
        print("you win")
    elif computer_choice>user_choice:
        print("you loose")
    

    



