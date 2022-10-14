from random import randint
from random import shuffle
# random
# Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
#show you two useful functions for now.
print("random")
dice1 = randint(1,7)
print(f"dice1 : {dice1}")
dice2 = randint(1,7)
print(f"dice2 : {dice2}")
rolledDoubles = dice1 == dice2
if rolledDoubles:
  print("You rolled a double")
else: print ("Not doubles")
if dice1 == dice2 == 1:
  print("You rolled snake eyes")
else: print("You did not roll snake eyes")


#practice with shuffle
my_list = range(1,51)
print("my new list")
print(list(my_list))
my_list = list(my_list)
shuffle(my_list)
print(my_list)

big_list = randint(1,201)
print(big_list)
if big_list % 2 ==0:
  print("odd")
else: 
  print("even")