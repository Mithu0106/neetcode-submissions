class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for char in nums :
            if char in d:
                return True
            d.add(char)
        return False