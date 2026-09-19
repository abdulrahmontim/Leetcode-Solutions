class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0

        min_len = float("infinity")
        min_chars = ""
        min_start = 0

        need = dict()
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        required = len(t)

        for right in range(len(s)):
            right_char = s[right]

            if right_char in need:
                if need[right_char] > 0:
                    required -= 1

                need[right_char] -= 1
        
            while required == 0:
                # there's a valid window
                #pop from left while remaining valid, popping means need[char] increases
                # if need[char] > 0 => needs to stop, renders the window in valid
                curr_window_len = (right - left) + 1
                if curr_window_len < min_len:
                    min_len = curr_window_len
                    min_start = left
                
                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        required += 1
                
                left += 1


        return s[min_start:min_start+min_len] if min_len !=float("inf") else ""






