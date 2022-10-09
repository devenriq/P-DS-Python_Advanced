from __future__ import division


def make_division_by(n):

    def division(x):
        return x / n

    return division


def run():
    division_by_10 = make_division_by(10)

    print(division_by_10(10))


if __name__ == "__main__":
    run()
