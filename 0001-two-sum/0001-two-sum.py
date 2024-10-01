class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complement_map:
                return [complement_map[complement], i]
            
            complement_map[num] = i
        
        return []