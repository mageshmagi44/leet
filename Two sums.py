class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash:
                return [i,hash[diff]]
            else:
                hash[n]=i
