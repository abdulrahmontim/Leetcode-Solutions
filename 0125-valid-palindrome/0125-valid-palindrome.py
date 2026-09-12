class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)


        start_pointer = 0
        end_pointer = l - 1


        while (start_pointer < end_pointer):

            while not s[start_pointer].isalnum() and start_pointer < end_pointer:
                start_pointer += 1
            
            while not s[end_pointer].isalnum() and start_pointer < end_pointer:
                end_pointer -= 1
            
            if (s[start_pointer].lower() != s[end_pointer].lower()):
                return False
            
            start_pointer += 1
            end_pointer -= 1
        
        return True
