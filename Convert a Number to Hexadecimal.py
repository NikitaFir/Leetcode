class Solution:
    def toHex(self, num):

        hex_digits = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        result = ""

        if num == 0:
            return '0'

        if num < 0:
            num += pow(2, 32)

        while num != 0:
            result = hex_digits[num % 16] + result
            num //= 16

        return result

print(Solution.toHex(0,26))
print(Solution.toHex(0,-1))

