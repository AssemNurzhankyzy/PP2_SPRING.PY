class PrimeChecker:
    def __init__(self, values):
        self.values = values

    def check_prime(self, value):
        if value < 2:
            return False
        for divisor in range(2, int(value**0.5) + 1):
            if value % divisor == 0:
                return False
        return True

    def get_prime_values(self):
        return list(filter(lambda num: self.check_prime(num), self.values))

size = int(input("Enter count of numbers: "))
num_list = []

for _ in range(size):
    num_list.append(int(input("Enter number: ")))

prime_finder = PrimeChecker(num_list)
print(prime_finder.get_prime_values())
