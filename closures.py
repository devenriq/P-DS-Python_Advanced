# def main():
#     a = 1

#     def nested():
#         print(a)

#     return nested

# my_func = main()
# my_func()


def make_multiplier(x):

    def multiplier(n):
        return n * x

    return multiplier


times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# def make_repeater_of(n):

#     def repeated(string):
#         assert type(string) == str, "solo pedes usar cadenas"
#         return string * n

#     return repeated

# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5('Hola'))

# if __name__ == '__main__':
#     run()
