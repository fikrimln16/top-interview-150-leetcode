class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}

        #tips 1 counter
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        #tips 2 cari nilai kemunculan paling gede
        max_freq = max(count.values())

        #tips 3 mencari nilai apakah ada kemunculan yang sama dengan max
        found_max = [num for num, val in count.items() if val == max_freq]

        #tips 4 kalikan kemunculan dengan kemunculan tertinggi
        return len(found_max) * max_freq

        

        