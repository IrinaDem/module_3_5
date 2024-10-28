def get_multiplied_digits(number):
    str_number = str(number)

    if all(digit == '0' for digit in str_number):
        return 1

    first = int(str_number[0])

    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)


