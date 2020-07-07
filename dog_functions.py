def foodOrder(smallDogs,mediumDogs,largeDogs,surplusFood):
    foodNeededNextMonth = (float(smallDogs) * 10) + (float(mediumDogs) * 20) + (float(largeDogs)* 30)
    foodOrder = round((float(foodNeededNextMonth) - float(surplusFood)) * 1.20,1)
    return foodOrder
    
def overCapacity(smallDogs,mediumDogs,largeDogs):
    totalDogs = float(smallDogs) + float(mediumDogs) + float(largeDogs)
    if totalDogs > 30 or totalDogs < 1: 
        print ("Number of dogs doesnt match owner capacity")
        exit()
    
   

