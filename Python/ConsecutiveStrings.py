# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

def longest_consec(strarr, k):
    # your code
    if len(strarr) == 0 or k > len(strarr)  == 0 or k <= 0:
        return ''
    answer_string = ''
    longest_string = ''
    longest_index = 0
    for i in range(k):
        for i in range(len(strarr)):
            if len(strarr[i]) > len(longest_string):
                longest_string = strarr[i]
                longest_index = i
        answer_string += strarr.pop(longest_index)
    return answer_string
            
        

print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))