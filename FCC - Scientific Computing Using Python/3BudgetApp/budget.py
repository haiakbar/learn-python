from math import floor

class Category:
    
    def __init__(self, category):
        self.ledger = list()
        self.category = category
    
    def deposit(self, amount, description=''):
        if amount > 0:
            self.ledger.append({"amount":amount, "description":description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) and amount != 0:
            self.ledger.append({"amount":amount*-1, "description":description})
            return True
        return False
    
    def get_balance(self):
        return sum([val["amount"] for val in self.ledger])
    
    def transfer(self, amount, target):
        if self.check_funds(amount) and amount != 0:
            self.withdraw(amount, 'Transfer to {}'.format(target.category))
            target.deposit(amount, 'Transfer from {}'.format(self.category))
            return True
        else:
            return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        self.lines = list()
        self.lines.append('{:*^30}'.format(self.category))
        for log in self.ledger:
            line = '{:23.23s}{:>7.2f}'.format(log["description"], log["amount"])
            self.lines.append(line)
        self.lines.append('Total: {:.2f}'.format(self.get_balance()))
        return '\n'.join(self.lines)

def create_spend_chart(cat_list):
    
    lines = list()
    cat_spending = list()
    cat_chars = list()
    spending_total = 0
        
    for cat in cat_list:
        spending = sum([item["amount"] for item in cat.ledger if item["amount"] < 0])
        cat_spending.append({"category":cat.category, "amount":spending})
        spending_total += spending
    
    for item in cat_spending:
        item_amount = item["amount"]
        #item["percentage"] = round((item_amount/spending_total)*10)*10
        item["percentage"] = floor((item_amount/spending_total)*10)*10
    
    header = 'Percentage spent by category'
    lines.append(header)
    
    for i in range(100,-1,-10):
        line = '{:>3}|'.format(i)
        for cat in cat_spending:
            if cat["percentage"] >= i:
                line += ' o '
            else:
                line += '   '
        line += ' '
        lines.append(line)
    
    footer = '    ' + '---'*len(cat_spending) + '-'
    lines.append(footer)

    for item in cat_spending:
        chars = []
        for char in item["category"]:
            chars.append(char)
        cat_chars.append(chars)
    
    for i in range(max([len(cat_name) for cat_name in cat_chars])):
        line = ' '*4
        for chars in cat_chars:
            try:
                line += ' {} '.format(chars[i])
            except:
                line += ' '*3
        line += ' '
        lines.append(line)
    
    return '\n'.join(lines)