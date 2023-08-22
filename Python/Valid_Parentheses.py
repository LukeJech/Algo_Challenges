# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# iterate through the string - loop through half
# check first index compared to last index, repeat moving +1 index and -1 index from the back 
# check if parentheses match it's counterpart 

def isValid(s):
    if (len(s) % 2 != 0):
        return False
    array = []
    parentheses_match = {
        ')': '(',
        '}': '{',
        ']': '[',
        '(': None,
        '{': None,
        '[': None
    }
    for char in s:
        if not (parentheses_match[char]):
            array.append(char)
        else:
            if not (array):
                return False
            if(array[-1] == parentheses_match[char]):
                array.pop()
            else:
                return False
    if(array):
        return False
    return True





print(isValid("([}}])"))



    # if (len(s) % 2 != 0):
    #     return False
    
    # parentheses_match = {
    #     '(' : ')',
    #     '{': '}',
    #     '[': ']',
    #     ')': None,
    #     '}': None,
    #     ']': None
    # }
    # if(parentheses_match[s[0]] != s[1]):
    #     j = -1
    #     for i in range(int(len(s)/2)):
    #         if not (parentheses_match[s[i]] ):
    #             return False
    #         if(parentheses_match[s[i]] != s[j-i]):
    #             return False
    # else:
    #     for i in range(0,int(len(s)-1),2):
    #         if not (parentheses_match[s[i]] ):
    #             return False
    #         if (parentheses_match[s[i]] != s[i+1]):
    #             return False
    # return True