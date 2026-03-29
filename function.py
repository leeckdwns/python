def print_n_times(*values, n=2):

    for i in range(n):

        for value in values:

            print(value)

        print()

print_n_times('Hello', 'World', n=3)


def mul(*values):

    output = 1

    for value in values:

        output *= value
    return output

print(mul(5, 7, 9, 10))

