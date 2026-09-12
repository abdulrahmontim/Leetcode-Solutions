class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int size = nums.size();
        vector<int> res;

        vector<int> pref;
        // pref.push_back(1);
        int prod = 1;
        for (int i = 0; i < size; i++) {
            pref.push_back(prod);
            prod *= nums[i];
        }
        
        vector<int> suf(size);
        int rev_prod = 1;
        for (int i = size - 1; i >= 0; i--) {
            suf[i] = rev_prod;
            rev_prod *=  nums[i];
        }

        for (int i = 0; i < size; i++) {
            int x_prod = pref[i] * suf[i];
            res.push_back(x_prod);
        }

        return res;
    }
};