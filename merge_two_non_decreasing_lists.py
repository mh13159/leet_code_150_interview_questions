
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m=3
n=3

if nums1[0]==0:
    nums1 = nums2[:]
    print(nums1)
    exit()
nums2 = nums2[::-1]
for element in nums2:
    #print(element)
    nums1_non_zero= nums1[0:m]
    #print(nums1_non_zero)
    nums1_last_element = -1
    nums1_max = nums1_non_zero[nums1_last_element]
    #print(nums1_max)
    while element< nums1_max:
        #print(element)
        #print(nums1_max)
        nums1_last_element= nums1_last_element-1
        nums1_max = nums1_non_zero[nums1_last_element]
        #print(nums1_max)
        #print(nums1_last_element)
    if nums1[m+n+nums1_last_element]==0:
        nums1[m+n+nums1_last_element]=element
    else:
        print(nums1[m+n+nums1_last_element])
        nums1[m+n+nums1_last_element+1]=nums1[m+n+nums1_last_element]
        nums1[m+n+nums1_last_element]=element
    n-=1
    print(nums1)
