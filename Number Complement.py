class Solution(object):
    def findComplement(self, num):

        Bin = bin(num)
        Bin = Bin[2:]

        for i in range(0,len(Bin)):
            if Bin[i] == '1':
                Bin = Bin[:i] + '0' + Bin[i + 1:]
            else:
                Bin = Bin[:i] + '1' + Bin[i + 1:]

        return int(Bin, 2)

print(Solution.findComplement(0,5))
print(Solution.findComplement(0,1))