class Solution(object):
	def findDuplicates(self, nums):

		result = []
		check = {}

		for elem in nums:
			if elem in check:
				check[elem] = 1
			else:
				check[elem] = 0

		for elem in check:
			if check[elem] != 0:
				result.append(elem)

		return result

print(Solution.findDuplicates(0,[4,3,2,7,8,2,3,1]))