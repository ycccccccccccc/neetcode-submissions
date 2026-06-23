class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pastSum = nums[0];
        int maxSum = pastSum;

        for (int i = 1; i < nums.size(); i++) {
            if (pastSum < 0) pastSum = 0;
            pastSum += nums[i];

            if (pastSum > maxSum) {
                maxSum = pastSum;
            }
        }

        return maxSum;
    }
};
