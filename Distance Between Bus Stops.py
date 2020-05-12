class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):

        clockwise = 0

        if start < destination:
            for i in range(start,destination):
                clockwise += distance[i]

        elif start == destination:
            return distance[start]
        else:
            for i in range(destination,start):
                clockwise += distance[i]

        counterclockwise = sum(distance) - clockwise

        return min(clockwise, counterclockwise)


print(Solution.distanceBetweenBusStops(0,[1,2,3,4], 0,1))
print(Solution.distanceBetweenBusStops(0,[1,2,3,4],0,3))