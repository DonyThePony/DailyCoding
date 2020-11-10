def perfect_number(number):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)

    return str(number) + str(10 - sum_of_digits)

if __name__ == '__main__':
    print(perfect_number(13))
