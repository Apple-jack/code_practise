'''
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for n in nums:
            n_str = '%s' % n
            if dic.get(n_str) is None:
                dic[n_str] = 1
            else:
                dic[n_str] += 1

        for key in dic.keys():
            if dic[key] > int(len(nums) / 2):
                return int(key)

s = Solution()
ret = s.majorityElement([2,2,1,1,1,2,2])
print(ret)
# dic = dict()
# dic['0'] = 1
# dic['0'] += 2
# print(dic.get('0'))