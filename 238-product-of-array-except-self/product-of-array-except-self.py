class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)

        left_product = 1        
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1        
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]


        return answer

        

            
        