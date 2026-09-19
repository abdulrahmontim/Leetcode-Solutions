class Solution {
public:
    int search(vector<int>& nums, int target) {

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {

            int middle = (left + right) / 2;

            if (nums[middle] == target) return middle;

            // check sorted side and eliminate
            if (nums[middle] >= nums[left]) {// left sorted
                if (target >= nums[left] && target <= nums[middle]) {
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
            
            } else { // right sorted
                if (target >= nums[middle+1] && target <= nums[right]) {
                    left = middle + 1;
                } else {
                    right = middle - 1;
                }

            }
        }

        return -1;

        
    }
};