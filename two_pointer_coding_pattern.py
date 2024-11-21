
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        167. Two Sum II - Input Array Is Sorted
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= len(numbers).
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
        The tests are generated such that there is exactly one solution. You may not use the same element twice.
        Your solution must use only constant extra space.
        Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
        Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
        Example 3:
        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
        Constraints:
        2 <= len(numbers) <= 3 * 104
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.
        '''
        # We will take two pointer approach giving us time complexity of O(p1+p2) and space complexity of O(1)
        p1 = 0
        p2 = len(numbers)-1
    
        while p1<len(numbers)-1 and p2>0 and len(numbers)!=2:
            #print(p1,p2)

            #print(numbers[p1]+numbers[p2])
            if numbers[p1]+numbers[p2]==target:
                return [p1+1,p2+1]
            elif numbers[p2]+numbers[p1]<target :
                p1+=1
            else:
                p2-=1
        return [p1+1,p2+1]


solution = Solution()
k = solution.twoSum(numbers=[-3,3,4,90],target=0)
print(k)