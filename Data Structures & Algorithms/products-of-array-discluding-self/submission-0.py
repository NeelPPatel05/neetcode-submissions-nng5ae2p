class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ret = []
        zeros = 0
        for i in nums:
            if(i !=0 ):
                prod = prod * i
            else:
                zeros += 1
        print (prod)
        for j in nums:
            if (zeros >= 2):
                ret.append(0)
            elif (zeros == 1):
                if(j == 0):
                    ret.append(int(prod))
                else:
                    ret.append(0)
            elif (zeros == 0):
                ret.append(int(prod/j))


        return ret