class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for k, v in counter.items():
            if v > len(nums) // 2:
                return k

        return 0