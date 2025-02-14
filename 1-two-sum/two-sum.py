class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for idx, num in enumerate(nums):
            if num in m:
                return [idx, m[num]]
            m[target - num] = idx
        #skj dnakjndsakjndaskjsdnaskjndaskjdnaskjdnas
        