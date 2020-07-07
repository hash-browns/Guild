from dog_function import foodOrder
from dog_function import overCapacity

smallDogs = None
while smallDogs == None:
    try:
        smallDogs = input("How many small dogs need food?")
        if int(smallDogs) < 0:
           print('Value cant be less than zero.')
           smallDogs = None
    except ValueError:
        print('Numerical values only, please.')

mediumDogs  = None
while mediumDogs  == None:
    try:
        mediumDogs  = input("How many medium dogs need food?")
        if int(mediumDogs) < 0:
           print('Value cant be less than zero.')
           mediumDogs  = None
    except ValueError:
        print('Numerical values only, please.')

largeDogs  = None
while largeDogs  == None:
    try:
        largeDogs  = input("How many large dogs need food?")
        if int(largeDogs) < 0:
           print('Value cant be less than zero.')
           largeDogs  = None
    except ValueError:
        print('Numerical values only, please.')        

overCapacity(largeDogs,mediumDogs,smallDogs)

surplusFood = input("How much food was leftover from last month (in lbs)?")

result = foodOrder(smallDogs,mediumDogs,largeDogs,surplusFood)
print("Total lbs of food to order " + str(result))
