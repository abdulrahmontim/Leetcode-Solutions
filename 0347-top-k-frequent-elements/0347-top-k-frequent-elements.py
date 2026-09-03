from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # trying bucket sort :)

        num_freq = Counter(nums)

        freq_bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in num_freq.items():
            freq_bucket[freq].append(num)

        res = []
        for i in range(len(freq_bucket) - 1, 0, -1):
            for content in freq_bucket[i]:
                res.append(content)

                if len(res) == k:
                    return res
                