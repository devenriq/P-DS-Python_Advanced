# def main():
#     a = 1

#     def nested():
#         print(a)

#     return nested

# my_func = main()
# my_func()

# def make_multiplier(x):

#     def multiplier(n):
#         return n * x

#     return multiplier

# times10 = make_multiplier(10)
# times4 = make_multiplier(4)

# print(times10(3))
# print(times4(5))
# print(times10(times4(2)))


def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "Solo puedes usar cadenas"
        return string * n

    return repeater


def run():
    repeater_of_10 = make_repeater_of(10)
    repeater_of_2 = make_repeater_of(2)

    print(repeater_of_10('Sucaritas'))
    print(repeater_of_2('Hola '))
    # print(repeater_of_10(2))


if __name__ == '__main__':
    run()
