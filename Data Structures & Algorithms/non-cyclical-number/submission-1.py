class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.nextNumber(n)
            if n in seen:
                return False
            seen.add(n)

        return True
            

    def nextNumber(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total = total + (digit)**2
            n = n // 10
        return total



        