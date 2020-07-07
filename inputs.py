from dog_functions import foodOrder
from dog_functions import overCapacity

while True: 
  try:
      smallDogs = int(input("How many small dogs need food?"))
      assert(smallDogs >= 0), 'Number must be bigger than or equal to 0'
  except ValueError:
        print('Numerical values only, please.')
  else:
      break

while True: 
  try:
      mediumDogs = int(input("How many medium dogs need food?"))
      assert(mediumDogs >= 0), 'Number must be bigger than or equal to 0'
  except ValueError:
        print('Numerical values only, please.')
  else:
      break 

while True: 
  try:
      largeDogs = int(input("How many large dogs need food?"))
      assert(largeDogs >= 0), 'Number must be bigger than or equal to 0'
  except ValueError:
        print('Numerical values only, please.')
  else:
      break                   

overCapacity(largeDogs,mediumDogs,smallDogs)

while True: 
  try:
      surplusFood = int(input("How much food was leftover from last month (in lbs)?"))
      assert(surplusFood >= 0), 'Number must be bigger than or equal to 0'
  except ValueError:
        print('Numerical values only, please.')
  else:
      break 

result = foodOrder(smallDogs,mediumDogs,largeDogs,surplusFood)
print("Total lbs of food to order " + str(result))
