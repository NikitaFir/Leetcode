class MinStack(object):

    def __init__(self):
        self.minStack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.minStack.append(x)
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        self.minStack.pop()
        """
        :rtype: None
        """

    def top(self):
        return self.minStack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return min(self.minStack)
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()