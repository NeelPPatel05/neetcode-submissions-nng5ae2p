class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) < sum(cost)):
            return -1
        for i in range(0, len(gas)):
            curgas = 0
            solution = True
            for j in range(len(gas)):
                cur_stop = (i + j)%len(gas)
                curgas += gas[cur_stop] - cost[cur_stop]
                if(curgas < 0):
                    solution = False
                    break
            if (solution == True):
                return i
        return -1