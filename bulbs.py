class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [1] * (n + 1)
        bulbs[0] = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                bulbs[i] = 0
        if n >= 3:
            for j in range(3, n):
                i = j
                while i <= n:
                    if bulbs[i] == 0:
                        bulbs[i] = 1
                    else:
                        bulbs[i] = 0
                    i += j

            if bulbs[-1] == 0:
                bulbs[-1] = 1
            else:
                bulbs[-1] = 0
        return sum(bulbs)

s = Solution()
ret = s.bulbSwitch(3)
print(ret)