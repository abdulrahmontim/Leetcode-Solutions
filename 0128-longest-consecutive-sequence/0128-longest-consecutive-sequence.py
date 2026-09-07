class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()


        last_seq = None
        max_seq = 0
        curr_max_seq = 0
        for i in range(len(nums) - 1):
            if (nums[i] + 1) == nums[i+1]:
                curr_max_seq += 1
                max_seq = max(curr_max_seq, max_seq)
            elif (nums[i] == nums[i + 1]):
                ...
            else:
                curr_max_seq = 0

        return max_seq + 1 if nums else 0