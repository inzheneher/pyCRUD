print("In odds __name__ is ", __name__)


def get_odds(numbers):
    odds = [n for n in numbers if n % 2 != 0]
    return odds


def main(args):
    try:
        odds_until = int(args[1])
    except ValueError:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)

    numbers = range(odds_until)
    print(get_odds(numbers))


if __name__ == '__main__':
    import sys
    main(sys.argv)
