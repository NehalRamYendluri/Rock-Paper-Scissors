import random
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
MyList = [rock,paper,scissors]

# print(f"{rock}\n{paper}\n{scissors}")
opt=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors : "))
Comp_opt = random.randint(0,2)

if opt<0 or opt>2:
  print("You have chosen wrong option.You Lost 😭 ")
else:
  print(f"You have chosen {MyList[opt]} \n")
  print(f"Computer have chosen {MyList[Comp_opt]} \n")
  if(opt==0 and Comp_opt==2) or (opt==2 and Comp_opt==1) or (opt==1 and Comp_opt==0):
    print("You Won!!! 😀")
  elif(opt==Comp_opt):
    print("It's a draw 😑")
  else:
    print("You Lost 😭")
