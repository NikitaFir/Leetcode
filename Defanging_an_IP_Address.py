class Solution(object):
    def defangIPaddr(self, address):

        i = 0
        while len(address)-1 != i:
            if address[i] == '.' :
                address = address[ :i] + "[.]" + address[ i + 1:]
                i += 1
            i += 1
        return address



print(Solution.defangIPaddr(0,"1.1.1.1"))
print(Solution.defangIPaddr(0,"255.100.50.0"))
