class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self


test = MathDojo()
add = test.add(2).add(2, 5, 1).add(2, 5).result
print("add:", add)
sub = test.subtract(2).subtract(2, 5, 1).subtract(2, 5).result
print("subtract:", sub)
add_sub = test.add(2).add(2, 5, 1).subtract(2, 5).result
print("add&subtract:", add_sub)
