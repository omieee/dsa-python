class Recursion_Practice:
    def factorial(self, num: int) -> int:
        if num <= 1:
            return 1
        else:
            return num * self.factorial(num - 1)
