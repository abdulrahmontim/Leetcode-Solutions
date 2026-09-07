class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_seq = 0
        curr_max_seq = 0

        for num in nums:
            if num - 1 not in nums:
                curr_max_seq = 1
                curr_num = num

                while (curr_num + 1 in nums):
                    curr_num +=1
                    curr_max_seq += 1
            
                max_seq = max(max_seq, curr_max_seq)
        
        return max_seq





            
        return max_seq