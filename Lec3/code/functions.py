def square(x):
    return x * x


def main():
    # Old string format syntax
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

    print("---------------------")

    # String format for Python 3
    for i in range(10):
        print(f"{i} squared is {square(i)}")

if __name__ == '__main__':
    main()
