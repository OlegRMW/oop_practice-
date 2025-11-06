class Account:
    def __init__(self, owner, balance, interest_rate=0, monthly_fee=0, transactions=0, limit=0):
        self.__owner = owner
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__monthly_fee = monthly_fee
        self.__transactions = transactions
        self.__limit = limit

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.__balance = value

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if value < 0:
            raise ValueError("Процентная ставка не может быть отрицательной")
        self.__interest_rate = value

    @property
    def monthly_fee(self):
        return self.__monthly_fee

    @monthly_fee.setter
    def monthly_fee(self, value):
        if value < 0:
            raise ValueError("Комиссия не может быть отрицательной")
        self.__monthly_fee = value

    @property
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        if value < 0:
            raise ValueError("Количество транзакций не может быть отрицательным")
        self.__transactions = value

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValueError("Лимит не может быть отрицательным")
        self.__limit = value

    def info(self):
        print(f"Владелец: {self.__owner}, Баланс: {self.__balance}, "
              f"Процентная ставка: {self.__interest_rate}%, "
              f"Месячная комиссия: {self.__monthly_fee}, Лимит: {self.__limit}")

    def account_type(self):
        return "Базовый счёт"

    def features(self):
        return "Обычные банковские операции"

    def calculate(self):
        """Вычисляет годовой доход от процентов"""
        return self.__balance * self.__interest_rate / 100


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

accounts = [base_acc, save_acc, check_acc]

for acc in accounts:
    print(f"\nТип счёта: {acc.account_type()}")
    acc.info()
    print("Особенности:", acc.features())
    print("Рассчитанное значение:", acc.calculate())
