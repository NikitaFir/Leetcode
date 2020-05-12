class MyHashMap(object):

    def __init__(self):
        self.val = None
        self.ke = None
        pair = [self.ke,self.val]
        self.all = []
        self.all.append(pair)

        """
        Initialize your data structure here.
        """

    def put(self, key, value):

        for i in range(0,len(self.all)):
            if self.all[i][0] == key:
                self.all[i][1] = value
                return None
        self.ke = key
        self.val = value
        pair = [self.ke, self.val]
        self.all.append(pair)

        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """

    def get(self, key):

        for i in  range(0,len(self.all)):
            if self.all[i][0] == key:
                return self.all[i][1]
        return -1

        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """

    def remove(self, key):
        i = 0
        while i != len(self.all):
            if self.all[i][0] == key:
                del self.all[i]
                i -= 1
            i += 1
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """

# Your MyHashMap object will be instantiated and called as such:
hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))             #returns 1
print(hashMap.get(3))          # returns -1 (not found)
hashMap.put(2, 1)          # update the existing value
print(hashMap.get(2))            # returns 1
hashMap.remove(2)          # remove the mapping for 2
print(hashMap.get(2))           # returns -1 (not found)