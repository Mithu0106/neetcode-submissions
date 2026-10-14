class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1 :
            return 0
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        print(nums)
        maxlen = 0 
        l = 0
        for r in range(len(nums)):
            if r>0 and nums[r-1] + 1 != nums[r] :
                l = r 
            maxlen = max(maxlen , r-l+1)
        return maxlen











        # lenc = 0 
        # for i in nums :
        #     cons = []
        #     cons.append(i)
        #     curr = i
        #     for num in nums :
        #         if num-1 == curr :
        #             cons.append(num)
        #             curr = num
        #     if len(cons) > lenc:
        #         lenc = len(cons)
        # return lenc 
