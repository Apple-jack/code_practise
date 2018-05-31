def minNumberInRotateArray(rotateArray):
    l = len(rotateArray)
    if l == 0:
        return 0
    if l == 1:
        return rotateArray[0]
    low = 0
    high = l - 1
    c_min = rotateArray[high]
    while low <= high:
        mid = int(high - (high - low) / 2)
        print(mid)
        if rotateArray[mid] <= rotateArray[mid + 1] and rotateArray[mid] <= c_min:
            c_min = rotateArray[mid]
            high = mid - 1
        else:
            low = mid + 1

    return c_min

# print(minNumberInRotateArray([4,4,4,4,4,1,2,2,2,2,2,2,2,2,2,2,3,4]))

class Solution:
    def __init__(self):
        self.dp = [0] * 40
        self.dp[1] = 1
        self.dp[2] = 1

    def Fibonacci(self, n):
        # write code here
        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]

s = Solution()
for i in range(1, 40):
    print(s.Fibonacci(i))