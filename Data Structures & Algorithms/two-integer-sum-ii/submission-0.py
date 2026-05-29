class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ind = 0
        r_ind = len(numbers) - 1

        while l_ind < r_ind:
            l_num = numbers[l_ind]
            r_num = numbers[r_ind]

            if l_num + r_num == target:
                return [l_ind + 1, r_ind + 1]
            elif l_num + r_num < target:
                l_ind += 1   # sum too small, move left pointer up
            else:
                r_ind -= 1   # sum too big, move right pointer down

        return []