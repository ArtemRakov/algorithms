class Lucky:
    def __init__(self, n):
        self.n = n
        self.count = 0


    def solve(self):
        def lucky_helper(digit, sum_first, sum_last):
            if digit == self.n:
                if sum_first == sum_last:
                    self.count += 1
                
                return
            
            for a in range(10):
                if digit < self.n / 2:
                    lucky_helper(digit + 1, sum_first + a, sum_last)
                else:
                    lucky_helper(digit + 1, sum_first, sum_last + a)
        lucky_helper(0, 0, 0)
        return self.count