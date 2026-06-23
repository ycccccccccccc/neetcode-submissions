class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxPosition = nums[0];

        for (int position = 1; position < nums.size(); position++) {
            if (maxPosition < position) {
                return false;
            }
            int nextPosition = position + nums[position];
            if (nextPosition > maxPosition) maxPosition = nextPosition;
        }

        return true;
    }
};
