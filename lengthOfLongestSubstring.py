class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        substring = []
        for ch in s:
            if ch in substring:
                substring = substring[substring.index(ch) + 1:] + [ch]
            else:
                substring.append(ch)
                maxLength = max(maxLength, len(substring))
        return maxLength
