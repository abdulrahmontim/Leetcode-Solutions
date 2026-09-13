class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        total_max = 0


        start_pointer = 0
        end_pointer = n -1 
    

        while start_pointer < end_pointer:
            total_max = max(total_max, min(height[start_pointer], height[end_pointer]) * (end_pointer - start_pointer))

            if height[start_pointer] < height[end_pointer]:
                start_pointer += 1
            elif height[start_pointer] > height[end_pointer]:
                end_pointer -= 1
            else:
                start_pointer += 1
                end_pointer -= 1

        return total_max