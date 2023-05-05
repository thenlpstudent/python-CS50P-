import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            names.append(input("Input: "))
        except EOFError:
            print(get_sentence(p, names))
            break


def get_sentence(p, names):
    if len(names) == 0:
        return
    prefix = "Adieu, adieu, to "
    suffix = p.join(names)
    return f"{prefix}{suffix}"


if __name__ == "__main__":
    main()
