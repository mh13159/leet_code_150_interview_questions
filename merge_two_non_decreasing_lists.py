class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Set up pointers for nums1 and nums2 starting from the end
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Traverse nums1 and nums2 from the end to the beginning
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in nums2, copy them
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]

# Instantiate the Solution class
solution = Solution()

# Define multiple test cases
test_cases = [
    {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
    {"nums1": [1], "m": 1, "nums2": [], "n": 0},
    {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
    {"nums1": [4, 5, 6, 0, 0, 0], "m": 3, "nums2": [1, 2, 3], "n": 3},
    {"nums1": [2, 0], "m": 1, "nums2": [1], "n": 1},
]

# Execute each test case
for i, case in enumerate(test_cases):
    nums1, m, nums2, n = case["nums1"], case["m"], case["nums2"], case["n"]
    solution.merge(nums1, m, nums2, n)
    print(f"Test case {i+1}: {nums1}")
