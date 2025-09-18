class PowerOfTwoChecker:
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        # число является степенью двойки, если оно больше 0 и у него только 1 бит равен 1
        return n > 0 and (n & (n - 1)) == 0


# проверяем числа от 1 до 128
for i in range(1, 129):
    print(i, PowerOfTwoChecker.is_power_of_two(i))
