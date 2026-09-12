class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        start_pointer = 0
        end_pointer = n - 1

        while start_pointer < end_pointer:
            pointer_add = numbers[start_pointer] + numbers[end_pointer]

            if pointer_add == target:
                return [start_pointer + 1, end_pointer + 1]
            
            else:
                if pointer_add > target:
                    end_pointer -= 1
                
                if pointer_add < target:
                    start_pointer += 1
            
        