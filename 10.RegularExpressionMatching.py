class Solution(object):
    def isMatch(self, s, p):
        # Create a memoization table to store the results of subproblems
        memo = {}

        # Recursive function with memoization to check if the pattern matches the string
        def matchHelper(s_index, p_index):
            # Check if we have already computed the result for this subproblem
            if (s_index, p_index) in memo:
                return memo[(s_index, p_index)]

            # Base case: If both indexes reached the end of their strings, it's a match
            if p_index == len(p):
                memo[(s_index, p_index)] = s_index == len(s)
                return memo[(s_index, p_index)]

            # Check if current characters match or pattern character is '.'
            current_match = s_index < len(s) and (s[s_index] == p[p_index] or p[p_index] == '.')

            # If the next character in the pattern is '*'
            if p_index + 1 < len(p) and p[p_index + 1] == '*':
                # Case 1: '*' matches 0 characters, skip '*' and the preceding character in the pattern
                # Case 2: '*' matches 1 or more characters, keep the preceding character in the pattern
                memo[(s_index, p_index)] = matchHelper(s_index, p_index + 2) or (current_match and matchHelper(s_index + 1, p_index))

            else:
                # If current characters match, move to the next characters in both strings
                if current_match:
                    memo[(s_index, p_index)] = matchHelper(s_index + 1, p_index + 1)
                else:
                    memo[(s_index, p_index)] = False

            return memo[(s_index, p_index)]

        return matchHelper(0, 0)
