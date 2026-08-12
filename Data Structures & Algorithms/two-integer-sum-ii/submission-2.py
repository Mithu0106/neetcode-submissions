class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)) :
            need = target - numbers[i]
            if need in d :
                op = [i+1,d[need]]
                return(sorted(op))
            d[numbers[i]] = i+1
        return []
