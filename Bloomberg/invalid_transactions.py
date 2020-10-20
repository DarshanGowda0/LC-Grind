class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

class Solution:
    def invalidTransactions(self, transactions):
        res = set()
        transactions = [Transaction(*t.split(',')) for t in transactions] # O(n) time
        transactions.sort(key=lambda t: t.time) # O(nlogn) time

        for i in range(len(transactions)): # O(n^2) time
            t1 = transactions[i]
            if t1.amount > 1000:
                res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
            for j in range(i+1, len(transactions)):
                t2 = transactions[j]
                if t2.name == t1.name and t2.time-t1.time <= 60 and t2.city != t1.city:
                    res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
                    res.add("{},{},{},{}".format(t2.name, t2.time, t2.amount, t2.city))

        return list(res)