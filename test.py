import budget


food = budget.Category('Food')

food.deposit(1000, 'Innitial Deposit')
food.withdraw(15.76, 'McDonalds')
food.withdraw(150, 'Groceries')
food.withdraw(10.15, 'Boba')
food.deposit(50, 'Honey gives me $')

cat = budget.Category('Cat')

food.transfer(400, cat)
cat.withdraw(50, 'Food')

# print(food)
# print(cat)

print(food.get_balance())
print(food.check_funds(300))


