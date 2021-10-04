'''
FreeCodeCamp budget calculator project
https://replit.com/@JosefRein/boilerplate-budget-app#main.py

By Josef Rein
'''


class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []

    def deposit(self, d_amount, d_description=""):
        if len(d_description) > 23:
            d_description = d_description[0:23]

        self.d_dict = dict(amount=d_amount, description=d_description)
        self.ledger.append(self.d_dict)

    def withdraw(self, w_amount, w_description=""):
        if len(w_description) > 23:
            w_description = w_description[0:23]

        if w_amount > 0:
            w_amount = w_amount*-1
        self.w_dict = dict(amount=w_amount, description=w_description)
        self.ledger.append(self.w_dict)

    def get_balance(self):
        values = [sub['amount'] for sub in self.ledger]
        balance = sum(values)
        return round(balance, 2)

    def transfer(self, amount, recipient):
        if self.get_balance() < amount:
            print("Insufficient funds")
            return False

        self.withdraw(amount,
                      'Transfer to {}'.format(recipient.cat_name))

        recipient.deposit(
            amount, 'Transfer from {}'.format(self.cat_name))

        print('Transfer successful!')
        return True

    def check_funds(self, amount):
        current_funds = self.get_balance()
        if amount > current_funds:
            return False
        else:
            return True

    def __str__(self):

        title = '{}\n'.format(self.cat_name.center(30, '*'))

        items = ''
        for i in self.ledger:
            items += i['description'].ljust(23) + \
                format(i['amount'], '.2f').rjust(7) + '\n'

        # line = '_' * 30

        balance = self.get_balance()
        total = 'Total: {:.2f}'.format(balance)
        # total = '\nTotal:'.ljust(23) + '{:.2f}'.format(balance).rjust(8)

        return title + items + total + '\n'


def create_spend_chart(li):

    total_deposits = 0
    for i in li:
        for x in i.ledger:
            if x['amount'] > 0 and 'Transfer from' not in x['description']:
                total_deposits += x['amount']

    withdraws = []
    for i in li:
        withdraws.append(sum(x['amount']*-1 for x in i.ledger if x['amount']
                         < 0 and 'Transfer to' not in x['description']))

    percentages = list(
        map(lambda x: round(x/total_deposits*100, 2), withdraws))

    # title = 'Percentage spent by category\n'

    return percentages


# print(create_spend_chart([food, clothing, auto]))


# [{"amount": amount, "description": description},
# {"amount": amount, "description": description}]
