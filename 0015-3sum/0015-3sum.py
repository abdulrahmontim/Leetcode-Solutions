class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = list()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            first_num = nums[i]
            start_pointer = i + 1
            end_pointer = n - 1

            while start_pointer < end_pointer:
                three_sum_add = first_num + nums[start_pointer] + nums[end_pointer]
                if three_sum_add == 0:
                    res.append([first_num, nums[start_pointer], nums[end_pointer]])

                    start_pointer += 1
                    end_pointer -= 1

                    while start_pointer < end_pointer and nums[start_pointer] == nums[start_pointer-1]:
                        start_pointer += 1
                
                elif three_sum_add < 0 and start_pointer < end_pointer:
                    start_pointer += 1
                elif three_sum_add > 0 and start_pointer < end_pointer:
                    end_pointer -= 1
            
        return res

  