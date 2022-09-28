def make_division_by(n):

    def division_of(x):
        return x / n

    return division_of


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))


if __name__ == '__main__':
    run()
