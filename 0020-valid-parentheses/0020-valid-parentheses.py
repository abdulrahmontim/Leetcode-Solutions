class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        
        stack = list()


        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if stack:
                    top = stack.pop()
                    if top != brackets[bracket]:
                        return False
                else:
                    return False

        return True if not stack else False




        