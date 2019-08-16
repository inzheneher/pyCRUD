def get_fibonacci(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return get_fibonacci(a - 2) + get_fibonacci(a - 1)


def main(args):
    try:
        fibonacci_numbers = int(args[1])
    except ValueError:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)

    print(get_fibonacci(fibonacci_numbers))


if __name__ == '__main__':
    import sys
    main(sys.argv)
