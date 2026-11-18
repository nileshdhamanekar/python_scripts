class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        for item in nums:
            if item in hash_set:
                return True
            else:
                hash_set.add(item)
        return False
