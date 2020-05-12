class Solution(object):
    def help(self, l, mas):
        mas.append(0)
        mas.append(1)
        for i in range(3, l+1):
            mas.append(Solution.search(self, i, mas))

    def search(self, i, mas):
        k = 0
        while i != 1:
            k += 1
            if i % 2 == 0:
                i //= 2
                if i < len(mas):
                    k += mas[i - 1]
                    break
            else:
                i = i * 3 + 1
                if i < len(mas):
                    k += mas[i - 1]
                    break
        return k

    def getKth(self, lo, hi, k):

        temp = []
        Solution.help(self, hi, temp)

        result = []
        for i in range(lo, hi+1):
            result.append([temp[i - 1], i])
        result.sort()
        return result[k - 1][1]


print(Solution.getKth(0, 12, 15, 2))
print(Solution.getKth(0, 1, 1, 1))

