# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# to check if each digit of n multiplied together is < 10
# if it's not we are going to have to again do the step before and check if it's < 10

def persistence(n):
    amount = 0 

    while n >= 10:
        n = str(n)
        total = n[0]
        for num in range(1,len(n)):
            total = int(total) * int(n[num])
        amount += 1
        n = total
    return amount

print(persistence(39))
print(persistence(4))
