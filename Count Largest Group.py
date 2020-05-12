class Solution(object):
        def extrafunc(self, n):
            a = 0
            while n != 0:
                a += n % 10
                n /= 10
            return a

        def countLargestGroup(self, n):

            a = [0] * 37

            for i in range(1, n + 1):
                a[int(Solution.extrafunc(self, i))] += 1

            a.sort()

            return a.count(a[36])

print(Solution.countLargestGroup(0, 13))
print(Solution.countLargestGroup(0, 2))
print(Solution.countLargestGroup(0, 15))
print(Solution.countLargestGroup(0, 24))
