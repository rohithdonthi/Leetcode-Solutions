from bisect import bisect_left, bisect_right

class Solution(object):
    def maximumCount(self, nums):
        pos_idx = bisect_left(nums, 1) 
        neg_idx = bisect_right(nums, -1)
        neg_count = neg_idx
        pos_count = len(nums) - pos_idx

        return max(neg_count, pos_count)