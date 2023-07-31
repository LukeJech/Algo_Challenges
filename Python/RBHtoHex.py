# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    # your code here :)
    round = lambda x: min(255, max(x, 0))
    r = round(r)
    g = round(g)
    b = round(b)
    
    hexcode = ''

    r_first_digit = int(r / 16)
    r = r % 16
    hexcode += str(convert_to_hex(r_first_digit)) 
    hexcode += str(convert_to_hex(r)) 

    g_first_digit = int(g / 16)
    g = g % 16
    hexcode += str(convert_to_hex(g_first_digit)) 
    hexcode += str(convert_to_hex(g)) 

    b_first_digit = int(b / 16)
    b = b % 16
    hexcode += str(convert_to_hex(b_first_digit)) 
    hexcode += str(convert_to_hex(b)) 

    return hexcode

def convert_to_hex(num):
    if num == 10:
        return 'A'
    if num == 11:
        return 'B'
    if num == 12:
        return 'C'
    if num == 13:
        return 'D'
    if num == 14:
        return 'E'
    if num == 15:
        return 'F'
    return num



print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(-25, 255, 300))