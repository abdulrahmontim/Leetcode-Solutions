class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;

        int longest = 0;
        set<int> seen;

        while (right < s.length()) {
            if (!seen.contains(s[right])) {
                seen.insert(s[right]);
                longest = max(longest, (right - left) + 1);
                right++;
            } else {
                seen.erase(s[left]);
                left++;
            }
        }

        return longest;
    }
};