class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)
        if s[0] == "0": return 0

        for i in range(1, len(s)):
            if s[i] == "0":
                if i == 0 or s[i-1] not in ("1", "2"):
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            elif 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] = dp[i-1] + dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[-1] 
