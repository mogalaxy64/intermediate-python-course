import random
def main():
  dice_sum = 0
  dice_sides = int(input('How many sides are on the dice?'))
  dice_rolls = int(input('How many dice do you want to roll?'))
  for i in range (0,dice_rolls):
    
    
    roll = random.randint(1,dice_sides)
    if roll == 1:
      print(f'Critical Fail! You rolled a {roll}')
    elif roll == dice_sides: 
      print(f'Damn son! You rolled a {roll}')
    else:
      print(f'You rolled a {roll}')
    dice_sum += roll
  print(f'Your total roll is {dice_sum}')

    	

if __name__== "__main__":
  main()
