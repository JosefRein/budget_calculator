import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(250, "groceries")
food.withdraw(300, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(1000)
clothing.withdraw(500)
clothing.withdraw(200)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(700)
dog = budget.Category("Dogs")
dog.deposit(1000, 'init')

print(food)
print(clothing)
print(dog)

print(create_spend_chart([food, clothing, auto, dog]))

