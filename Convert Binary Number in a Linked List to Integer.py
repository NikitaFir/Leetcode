# Definition for singly-linked list.
# Пределение элемента односвязного списка
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
    def getDecimalValue(self, head):

        BinaryNumber = []
        while (head) :
            BinaryNumber.append(str(head.val))
            head = head.next

        result =''.join(BinaryNumber)

        return int(result,2)
# -------------------------------------------------------
head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
L = LinkedList()
for i in range(0,len(head)):
    L.add(head[i])
# print(L)
# -------------------------------------------------------
print(Solution.getDecimalValue(0,L.first))