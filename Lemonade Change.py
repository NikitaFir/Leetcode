class Solution(object):
    def lemonadeChange(self, bills):

        bill_5 = 0
        bill_10 = 0

        for i in range(0, len(bills)):
            if bills[i] == 5:
                bill_5 += 1

            elif bills[i] == 10:
                if bill_5 == 0:
                    return False
                bill_5 -= 1
                bill_10 += 1

            elif bills[i] == 20:
                if bill_10 > 0 and bill_5 > 0:
                    bill_10 -= 1
                    bill_5 -= 1
                elif bill_5 > 2:
                    bill_5 -= 3
                else:
                    return False

        return True
print(Solution.lemonadeChange(0,[5,5,5,10,20]))
print(Solution.lemonadeChange(0,[5,5,10]))
print(Solution.lemonadeChange(0,[10,10]))
print(Solution.lemonadeChange(0,[5,5,10,10,20]))