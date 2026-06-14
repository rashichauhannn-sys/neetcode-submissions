class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map ={}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1

            else:
                freq_map[num] = 1
        sorted_freq = sorted(freq_map, key=freq_map.get, reverse= True)


        return sorted_freq[:k]