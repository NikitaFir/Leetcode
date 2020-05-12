class MyHashSet(object):

    def __init__(self):
        self.values = []

    def add(self, key):
        if self.values.count(key) >= 1:
            return None
        else:
            self.values.append(key)
        """
        :type key: int
        :rtype: None
        """

    def remove(self, key):
        i = 0
        while i !=  len(self.values):
            if self.values[i] == key:
                del self.values[i]
                break
            i += 1
        """
        :type key: int
        :rtype: None
        """

    def contains(self, key):
        for i in range(0,len(self.values)):
            if self.values[i] == key:
                return True
        return False
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """

hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    #returns true
print(hashSet.contains(3))   # returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))    # returns true
hashSet.remove(2)
print(hashSet.contains(2))    # returns false (already removed)