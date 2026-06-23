class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        sub_set = set(s[0])

        start = 0
        longest = 1
        for i in range(1,len(s)):
            while s[i] in sub_set:
                sub_set.remove(s[start])
                start += 1
            sub_set.add(s[i])
            longest = max(longest, i-start+1)
        return longest