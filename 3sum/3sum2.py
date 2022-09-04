class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited={}
        trackDuplicate=set()
        ans=set()
        for i, num1 in enumerate(nums):
            if num1 not in trackDuplicate:
                trackDuplicate.add(num1)
                for j,num2 in enumerate(nums[i+1:]):
                    currDiff= -num1-num2
                    if currDiff in visited and visited[currDiff]==i:
                        ans.add(tuple(sorted((currDiff,num1,num2))))      
                    visited[num2]=i
        return ans