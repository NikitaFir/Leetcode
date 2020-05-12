class Solution(object):
    def fairCandySwap(self, A, B):

        temp = set()
        x = 0
        y = 0

        for i in A:
            x += i

        for i in B:
            y += i
            temp.add(i)

        z = (y - x) / 2
        for i in A:
            if (i + z) in temp:
                return [i, int(i + z)]
        return None

print(Solution.fairCandySwap(0, [1,1], [2,2]))
print(Solution.fairCandySwap(0,[1,2], [2,3]))
print(Solution.fairCandySwap(0, [2], [1,3]))
