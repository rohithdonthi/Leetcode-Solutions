import collections
import bisect

class TimeMap(object):

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""

        times = self.store[key]
        left, right = 0, len(times) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if times[mid][0] <= timestamp:
                res = times[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
