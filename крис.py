def convert(number, from_base, to_base):
    number = int(number, from_base)

    if to_base == 2:
        return bin(number)
    elif to_base == 8:
        return oct(number)
    elif to_base == 10:
        return number
    elif to_base == 16:
        return hex(number)


print(convert("1010", 2, 10))
print(convert("25", 10, 2))
print(convert("17", 8, 16))
print(convert("FF", 16, 2))
