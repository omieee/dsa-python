class Recursion_Practice:
    def factorial(self, num: int) -> int:
        if num <= 1:
            return num
        else:
            return num * self.factorial(num - 1)
