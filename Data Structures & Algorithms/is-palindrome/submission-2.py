class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not ('a' <= s[l] <= 'z' or '0' <= s[l] <= '9'):
                l += 1
                
            while l < r and not ('a' <= s[r] <= 'z' or '0' <= s[r] <= '9'):
                r -= 1

            if l > r:
                break
                
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True