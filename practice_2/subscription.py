from datetime import date

class Subscription:
    def __init__(self, user: str, plan: str, start_date: date):
        self.__user = user
        self.__plan = plan
        self.__start_date = start_date

    def get_user(self):
        return self.__user

    def get_plan(self):
        return self.__plan

    def get_start_date(self):
        return self.__start_date

    def subscription_age(self) -> int:
        today = date.today()
        age = today.year - self.__start_date.year
        # если месяц или день еще не наступил
        if (today.month, today.day) < (self.__start_date.month, self.__start_date.day):
            age -= 1
        return age


sub1 = Subscription("Иванов И.", "Premium", date(2021, 3, 1))
sub2 = Subscription("Петров П.", "Basic", date(2022, 7, 15))

print("Подписка 1:")
print("Пользователь:", sub1.get_user())
print("План:", sub1.get_plan())
print("Дата начала:", sub1.get_start_date())
print("Возраст подписки:", sub1.subscription_age())

print("\nПодписка 2:")
print("Пользователь:", sub2.get_user())
print("План:", sub2.get_plan())
print("Дата начала:", sub2.get_start_date())
print("Возраст подписки:", sub2.subscription_age())
