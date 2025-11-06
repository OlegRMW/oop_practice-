class Account:
    def __init__(self, owner, balance, interest_rate=0, monthly_fee=0, transactions=0, limit=0):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        self.monthly_fee = monthly_fee
        self.transactions = transactions
        self.limit = limit

    def info(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance}, Процентная ставка: {self.interest_rate}%, "
              f"Месячная комиссия: {self.monthly_fee}, Лимит: {self.limit}")

    def account_type(self):
        return "Базовый счёт"

    def features(self):
        return "Обычные банковские операции"

    def calculate(self):
        return self.balance * self.interest_rate / 100


class Savings(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance, interest_rate)
        self.limit = balance * 0.2 

    def account_type(self):
        return "Сберегательный"

    def features(self):
        return "Высокая ставка, ограничение на снятие"

    def calculate(self):
        return self.balance * self.interest_rate / 100


class Checking(Account):
    def __init__(self, owner, balance, monthly_fee):
        super().__init__(owner, balance, monthly_fee=monthly_fee)

    def account_type(self):
        return "Текущий"

    def features(self):
        return "Бесплатные переводы, дебетовая карта"

    def calculate(self):
        return self.balance - self.monthly_fee * 12


base_acc = Account("Иван Иванов", 10000, interest_rate=3)
save_acc = Savings("Мария Петрова", 20000, 5)
check_acc = Checking("Олег Смирнов", 15000, 200)

for acc in [base_acc, save_acc, check_acc]:
    print(f"\nТип счёта: {acc.account_type()}")
    acc.info()
    print("Особенности:", acc.features())
    print("Рассчитанное значение:", acc.calculate())
