class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int size = nums.size();
        vector<int> res(size, 1);


        int prod = 1;
        for (int i = 0; i < size; i++) {
            res[i] = prod;
            prod *= nums[i];
        }
        
        int rev_prod = 1;
        for (int i = size - 1; i >= 0; i--) {
            res[i] *= rev_prod;
            rev_prod *= nums[i];
        }

        return res;
    }
};