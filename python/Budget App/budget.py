class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,"description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount,"description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for each in self.ledger:
            total += each["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, fund):
        total = 0
        for each in self.ledger:
            total += each["amount"]

        if total >= fund:
            return True
        else:
            return False

    def __str__(self):
        output = ""
        output += self.name.center(30,'*') + "\n"
        for each in self.ledger:
            amount = format(each["amount"],'.2f').rjust(7)
            description = each["description"][:23].ljust(23)
            output += description + amount + "\n"
        total = self.get_balance()
        output += "Total: " + str(total)
        return output


def create_spend_chart(categories):
    total_spent = 0
    categories_spent = list()
    longest = 0
    for category in categories:
        total_category_spent = 0
        for each in category.ledger:
            if each["amount"] < 0:
                total_spent += abs(each["amount"])
                total_category_spent += abs(each["amount"])
        categories_spent.append({"category":category.name,"total":total_category_spent})

        #get longest name
        longest =  len(category.name) if len(category.name) > longest else longest

    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        output += str(i).rjust(3) + "|"
        for category_spent in categories_spent:
            if category_spent["total"]/total_spent * 100 > i:
                output +="o".center(3)
            else:
                output +="".center(3)
        output += " \n"
    output += "".rjust(4) + "".center((len(categories)*3)+1,"-") + "\n"

    vertical_output = ""
    for i in range(0,longest,1):
        vertical_output = vertical_output + "".rjust(4)
        for category in categories:
            if len(category.name) > i:
                vertical_output +=category.name[i].center(3)
            else:
                vertical_output += "".center(3)
        vertical_output += " \n"

    output += vertical_output.rstrip() + "  "
    return output