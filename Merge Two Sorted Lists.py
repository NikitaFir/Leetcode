class Solution(object):
    def mergeTwoLists(self, l1, l2):

        arr1 = []
        arr2 = []
        while (l1):
            arr1.append(l1.val)
            l1 = l1.next
        while (l2):
            arr2.append(l2.val)
            l2 = l2.next

        arr2.extend(arr1)
        arr2.sort()

        end = None
        i = len(arr2) - 1
        result = None
        while i != -1:
            result = ListNode(arr2[i])
            result.next = end
            end = result
            i -= 1
        return result