class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialize pointers for both arrays
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2

        # Pointer for the current position in nums1
        p = m + n - 1

        # Merge elements into nums1 in reverse order
        while p1 >= 0 and p2 >= 0:
            # Compare elements and place the larger one at the end of nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, append them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]