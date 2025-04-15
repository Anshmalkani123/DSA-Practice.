class Solution(object):
        def lengthOfLongestSubstring(self, s):
        seen = set()
        max_length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            w = (r - l) + 1
            max_length = max(max_length, w)
            seen.add(s[r])
        
        return max_length