class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        maxLen = 0
        curLen = 0
        startIndex = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= startIndex:
                curLen = i - seen[c]
                startIndex = seen[c] + 1
            else:
                curLen += 1
            seen[c] = i
            maxLen = max(maxLen, curLen)
        return maxLen