def make_repeater_of(n):

    def repeated(string):
        assert type(string) == str, "solo pedes usar cadenas"
        return string * n

    return repeated


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))


if __name__ == '__main__':
    run()
