# coding = utf-8

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return None
        res = 0
        for i in range(2,n+1):
            res = (res+m)%i
        return res
