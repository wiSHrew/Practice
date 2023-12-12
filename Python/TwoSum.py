class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        answer = []
        for x in range(len(nums)):
            for y in range(len(nums)):
                allysa = nums[x] + nums[y]
                if x == y:
                    continue
                elif allysa == target:
                    answer = [x, y]

        return(answer)
        