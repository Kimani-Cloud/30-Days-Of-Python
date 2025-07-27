import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self):
        freq = Counter(self.data)
        mode_val, count = freq.most_common(1)[0]
        return {"mode": mode_val, "count": count}

    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        # List of tuples sorted by frequency descending
        return sorted([(v * len(self.data) / 100, k) for k, v in freq.items()], reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum: ", self.sum())
        print("Min: ", self.min())
        print("Max: ", self.max())
        print("Range: ", self.range())
        print("Mean: ", self.mean())
        print("Median: ", self.median())
        print("Mode: ", tuple(self.mode().values()))
        print("Variance: ", self.var())
        print("Standard Deviation: ", self.std())
        print("Frequency Distribution:", self.freq_dist())


# Test the Statistics class
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()



class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # list of dicts: {'desc': str, 'amount': float}
        self.expenses = []

    def add_income(self, desc, amount):
        self.incomes.append({'desc': desc, 'amount': amount})

    def add_expense(self, desc, amount):
        self.expenses.append({'desc': desc, 'amount': amount})

    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Balance: {self.account_balance()}")
        print("\nIncomes:")
        for inc in self.incomes:
            print(f"- {inc['desc']}: {inc['amount']}")
        print("\nExpenses:")
        for exp in self.expenses:
            print(f"- {exp['desc']}: {exp['amount']}")


# Test the PersonAccount class
account = PersonAccount("John", "Doe")
account.add_income("Salary", 3000)
account.add_income("Freelance", 1200)
account.add_expense("Rent", 1000)
account.add_expense("Food", 400)
account.account_info()
