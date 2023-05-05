def main(items={}):
    while True:
        try:
            item = input()
            items = add_item(items, item)
        except EOFError:
            print_items(items)
            break


def add_item(items, item):
    try:
        item = item.lower()
        items[item] += 1
    except KeyError:
        items[item] = 1
    return items


def print_items(items):
    for key in items:
        print(f"{items[key]} {key.upper()}")


if __name__ == "__main__":
    main()
