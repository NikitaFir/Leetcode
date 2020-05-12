import copy

class Solution:
	def minDeletionSize(self, A):

		result = 0
		L = len(A[0])

		for j in range(0, L):
			temp1 = []

			for word in A:
				temp1.append(word[j])

			temp2 = copy.deepcopy(temp1)
			temp2.sort()

			for i in range(0, len(temp1)):
				if temp1[i] != temp2[i]:
					result += 1
					break

		return result

print(Solution.minDeletionSize(0, ["cba","daf","ghi"]))
print(Solution.minDeletionSize(0, ["a","b"]))
print(Solution.minDeletionSize(0, ["zyx","wvu","tsr"]))
