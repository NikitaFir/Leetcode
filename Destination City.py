class Solution(object):
    def destCity(self, paths):

        temp1 = set()
        temp2 = set()
        for i in range(0,len(paths)):
            if paths[i][0] not in temp1:
                temp1.add(paths[i][0])
            if paths[i][1] not in temp2:
                temp2.add(paths[i][1])
        result = (temp2 - temp1.intersection(temp2)).pop()
        return result

print(Solution.destCity(0,[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(Solution.destCity(0,[["B","C"],["D","B"],["C","A"]]))
