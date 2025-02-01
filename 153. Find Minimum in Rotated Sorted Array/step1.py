class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_index = 0  # 探索対象の配列の左端インデックス
        right_index = len(nums) - 1
        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] > nums[right_index]:
                # 最小値がmid_indexより右側にある場合
                left_index = mid_index + 1
            else:
                # 最小値がmid_indexより左側にある場合
                right_index = mid_index
        return nums[left_index]
