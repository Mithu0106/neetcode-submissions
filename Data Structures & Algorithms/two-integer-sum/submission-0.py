class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        ans=[]
        for i in range (n) :
            diff = target - nums[i]
            if diff in d :
                ans.append(d[diff])
                ans.append(i)
                return ans
            d[nums[i]] = i