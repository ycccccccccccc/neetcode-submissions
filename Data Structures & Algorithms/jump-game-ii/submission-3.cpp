class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, n);
        int minStep = 0;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            minStep = min(minStep, dp[i]);
            int target = (i + nums[i] < n) ? (i + nums[i]) : (n - 1);
            dp[target] = min(dp[target], minStep + 1);
            ++minStep;
        }
        return dp[n-1];
    }
};
