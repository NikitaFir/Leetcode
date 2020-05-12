class Solution(object):
    def minimumAbsDifference(self, arr):

        result = []
        arr.sort()
        minimum = max(arr)

        for i in range(1, len(arr)):

            difference = arr[i] - arr[i - 1]

            if difference < minimum:
                result = [[arr[i - 1], arr[i]]]
                minimum = difference
            elif difference == minimum:
                result.append([arr[i - 1], arr[i]])


        return result

print(Solution.minimumAbsDifference(0, [4,2,1,3]))
print(Solution.minimumAbsDifference(0, [3,8,-10,23,19,-4,-14,27]))


