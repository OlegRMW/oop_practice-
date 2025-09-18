class PowerOfTwoChecker:
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


for i in range(1, 129):
    print(i, PowerOfTwoChecker.is_power_of_two(i))
