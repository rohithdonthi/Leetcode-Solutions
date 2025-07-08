import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEatAll(speed):
            time = 0
            for pile in piles:
                time += int(math.ceil(float(pile) / speed))
            return time <= h

        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canEatAll(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
