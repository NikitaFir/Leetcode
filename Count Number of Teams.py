class Solution(object):
    def numTeams(self, rating):

        if rating == []:
            return 0

        result = 0
        for j in range(1,len(rating)):
            i_menshe_j = 0
            i_bolshe_j = 0
            k_menshe_j = 0
            k_bolshe_j = 0
            for i in range(0, j):
                if rating[i] < rating[j]:
                    i_menshe_j += 1
                elif rating[i] > rating[j]:
                    i_bolshe_j += 1

            for k in range(j+1, len(rating)):
                if rating[j] < rating[k]:
                    k_bolshe_j +=1
                elif rating[j] > rating[k]:
                    k_menshe_j += 1

            result += i_menshe_j * k_bolshe_j + i_bolshe_j * k_menshe_j

        return result

print(Solution.numTeams(0,[2,5,3,4,1]))
print(Solution.numTeams(0,[1,2,3,4]))


