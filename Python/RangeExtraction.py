# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

def solution(arr):
    # start a new string we can append and return later
    return_string = ''
    # create a loop to go through the array range
    i = 0
    while i < (len(arr)-1):
        print('i is', i)
    # set a first number and then do a while loop to check if the neighbor numbers are +1 of the previous
        first_num = arr[i]
        steps = 0
        while(arr[i + steps] + 1 == arr[i+steps+1]):
            print(arr[i + steps], arr[i+steps+1])
            steps += 1
            if (arr[i+steps] == arr[-1]):
                break
        print('steps', steps)
    #once it's not +1, we can insert that first number to the last number as a range, as long as steps are more than 1
        if steps >= 2:
            return_string += f'{first_num}-{arr[i+steps]},'
        elif steps == 1:
            return_string += f'{first_num},'
            return_string += f'{arr[i+1]},'
        else:
            return_string += f'{first_num},'
        i += steps + 1
    if(arr[-1] -1 != arr[-2]):
        return_string += f'{arr[-1]},'
    return return_string[0:-1]



print(solution([-73, -71, -69, -67, -64, -62, -61, -58, -57, -54, -53, -50, -49, -47, -44, -43, -41, -38, -36, -33, -30]))