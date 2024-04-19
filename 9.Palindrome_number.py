class Solution(object):
    def isPalindrome(self, x):
        # Handle negative numbers and numbers ending with 0 (excluding 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        while x > reversed_number:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            x = x // 10

        # If the length of the original number is odd, we can ignore the middle digit
        # by dividing the reversed number by 10.
        return x == reversed_number or x == reversed_number // 10
