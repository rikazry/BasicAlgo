
print_format = "|%s|%s|%s|"
print(print_format %('1','2','3'))
print(print_format %('4','5','6'))
print(print_format %('7','8','9'))
print(print_format %(' ','0',' '))

number_lookup = {\
        1:[6,8],
        2:[7,9],
        3:[4,8],
        4:[3,9,0],
        6:[1,7,0],
        7:[2,6],
        8:[1,3],
        9:[2,4],
        0:[4,6],
        }
print(number_lookup)

def total_rec(n, start=1):
    total = 0
    if n == 1:
        total = 1
    else:
        for value in number_lookup[start]:
            total += total_rec(n-1, value)
    return total

print total_rec(20)
