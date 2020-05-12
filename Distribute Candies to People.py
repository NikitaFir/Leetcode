class Solution(object):
    def distributeCandies(self, candies, num_people):

        people = [0] * num_people
        i = 0
        c = 1
        while candies != 0:

            people[i] += c
            candies -= c

            if candies - c > 0:
                c += 1
            else:
                c = candies

            if i == num_people - 1:
                i = -1
            i += 1

        return people

print(Solution.distributeCandies(0, 7, 4))
print(Solution.distributeCandies(0,10, 3))
print(Solution.distributeCandies(0,90, 4))
