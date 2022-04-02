# (a ^ p + b ^ (p + 1) + c ^ (p + 2) + d ^ (p + 3) + ...) = n * k

def dig_pow(n, p):
    lst_of_number = []
    number = map(int, str(n))
    for i in number:
        lst_of_number.append(int(i))

    new_lst_of_number = counting(lst_of_number, p)
    new_number = sum(new_lst_of_number)

    if new_number % n == 0:
        k = new_number // n
        return k
    else:
        return -1



def counting(lst_of_number, p):

    count = 0
    stage = p
    new_lst_of_numbers = []

    while count != len(lst_of_number):
        x = lst_of_number[count] ** stage
        new_lst_of_numbers.append(x)
        count += 1
        stage += 1

    return new_lst_of_numbers