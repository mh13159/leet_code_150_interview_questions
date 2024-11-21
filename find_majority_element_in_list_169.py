'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        max_key_val = 0
        max_key  = 0
        for element in nums:
            
            if element not in result.keys():
                result[element]=1
                #print (result)
            else:
                #print('in else')
                result[element] = result[element]+1
                #print(result)
            if result[element]> max_key_val:
                print('max key')
                print(result[element])         
                max_key= element
                max_key_val=result[element]
                print(max_key_val)
                #print(max_key)
        return max_key
solution = Solution()
k = solution.majorityElement(nums=[0,0,1,1,1,2,3,3,3,3,4,5,6,6,7])
print(k)
