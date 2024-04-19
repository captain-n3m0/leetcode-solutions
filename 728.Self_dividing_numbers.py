class Solution(object):
    def selfDividingNumbers(number, left, right):
        number = str(number)
        if '0' in number:
            return False
        for digit_char in number:
            digit = int(digit_char)

            if int(number) % digit != 0:
                return False
        return True

number = 128
print(Solution().selfDividingNumbers(number, 1, 22))
