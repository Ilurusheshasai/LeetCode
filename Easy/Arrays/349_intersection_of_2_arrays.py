'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.
'''


class Solution:
    
    def get_list(self, list1, list2):
        l = []
        for elem in list1:
            if elem in list2 and elem not in l:
                l.append(elem)
        return l
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 >= l2:
            list1 = nums2
            list2 = nums1
        else:
            list1 = nums1
            list2 = nums2
        
        return self.get_list(list1, list2)
            