class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = {}
        
        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []

            anagram_groups[sorted_s].append(s)
        
        return list(anagram_groups.values())       