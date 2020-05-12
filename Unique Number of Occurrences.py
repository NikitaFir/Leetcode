class Solution(object):
    def uniqueOccurrences(self, arr):

        Occurrences = []

        for i in set(arr):
            Occurrences.append(arr.count(i))
        if len(Occurrences) == len(set(Occurrences)):
            return True
        else:
            return False

print(Solution.uniqueOccurrences(0,[1,2,2,1,1,3]))
print(Solution.uniqueOccurrences(0,[1,2]))
print(Solution.uniqueOccurrences(0,[-3,0,1,-3,1,1,1,-3,10,0]))