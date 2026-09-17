class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        count = dict()
        max_freq = [0, 0]


        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            if count[s[right]] > max_freq[0]:
                max_freq = [count[s[right]], s[right]]

            window_length = (right - left) + 1

            if (window_length - max_freq[0]) <= k:
                # valid
                # right increases itself - imp1
                longest = max(longest, window_length)

            else:
                # invalid window
                count[s[left]] -= 1
                # recompute max_freq?
                left += 1


        return longest







        