costOfbooks = 20
noOfbooks = int(input("How many books do you want to buy?" ))
money = int(input("How much money do you have? "))

totalCostBooks = costOfbooks * noOfbooks

if money >= totalCostBooks:
    print("You have enough money, go fo it!")
else:
    print(f"You need {totalCostBooks - money} to buy that number of books")

