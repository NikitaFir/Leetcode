# Definition for singly-linked list.
# Пределение элемента односвязного списка
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def Add(self,x):
        self.x =ListNode.__init__(self,x)

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    # Для распечатки списка
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' + str(current.val) + '\n'
            while current.next != None:
                current = current.next
                out += str(current.val) + '\n'
            return out + ']'
        return 'LinkedList []'
    # Очистка списка
    def clear(self):
        self.__init__()
    # Добавление элемента в конец списка
    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = ListNode(x)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = ListNode(x)

class Solution(object):
    def middleNode(self, head):

        k = 0
        copy = head
        while (head) :
            k += 1
            head = head.next
        mid = math.ceil(k / 2)
        i = 0
        while (copy):
            if i == mid:
                return copy
            else:
                i += 1
                copy = copy.next
# -------------------------------------------------------
# head = [1,2,3,4,5,6]
head = [1,2,3,4,5]
L = LinkedList()
for i in range(0,len(head)):
    L.add(head[i])
# print(L)
# -------------------------------------------------------
print(Solution.middleNode(0,L.first))