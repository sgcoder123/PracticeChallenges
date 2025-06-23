def square_digits(num):
    real_number = ""
    for n in str(num):
        digit = int(n)
        real_num = (digit*digit)
        real_number += str(real_num)
    return int(real_number)