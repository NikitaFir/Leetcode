class Solution(object):

    def is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def calPoints(self, ops):

       i = 0
       while i != len(ops):
            if Solution.is_number(self,ops[i]):
                i += 1
            elif ops[i] =='D':
                ops[i] = int(float(ops[i - 1])*2)
                i += 1
            elif ops[i] =='C':
                del ops[i]
                del ops[i-1]
                i -= 1
            elif ops[i] =='+':
                ops[i] = int(ops[i - 2]) + int(ops[i - 1])
                i +=1
       ops = [int(item) for item in ops]
       return sum(ops)

print(Solution.calPoints(0,["5","2","C","D","+"]))
print(Solution.calPoints(0,["5","-2","4","C","D","9","+","+"]))
print(Solution.calPoints(0,["36","28","70","65","C","+","33","-46","84","C"]))
print(Solution.calPoints(0,["57","D","-3","-58","D","77","+","C","+","+","38","78","-6","24","-46","+","31","20","D","-81"]))

