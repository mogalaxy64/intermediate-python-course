import random
def main():
  dice_sum = 0
  dice_rolls = 3
  for i in range (0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  print(f'Your total roll is {dice_sum}')

    	

if __name__== "__main__":
  main()
