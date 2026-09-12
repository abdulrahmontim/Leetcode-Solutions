class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_map = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sort_map:
                sort_map[sorted_word].append(word)
            else:
                sort_map[sorted_word] = [word]
        
        res = list()

        for key in sort_map:
            res.append(sort_map[key])
        
        return res
    

        