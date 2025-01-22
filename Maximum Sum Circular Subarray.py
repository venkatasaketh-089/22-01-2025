class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(array):
            max_sum = curr_max = array[0]
            for num in array[1:]:
                curr_max = max(num, curr_max + num)
                max_sum = max(max_sum, curr_max)
            return max_sum
        
        total_sum = sum(nums)
        max_kadane = kadane(nums)  
        min_kadane = kadane([-num for num in nums])  

        if max_kadane > 0:
            return max(max_kadane, total_sum + min_kadane)  
            return max_kadane 
