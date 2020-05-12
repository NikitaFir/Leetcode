class Solution(object):
    def lastStoneWeight(self, stones):

        while len(stones) != 1:
            s1 = stones.index(max(stones))
            x = max(stones)
            stones.pop(s1)
            s2 = stones.index(max(stones))
            y = max(stones)
            stones.pop(s2)
            z = abs(x - y)
            if x > y:
                stones.insert(s1,z)
            else:
                stones.insert(s2, z)
        return stones[0]

print(Solution.lastStoneWeight(0,[2,7,4,1,8,1]))