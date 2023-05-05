import emoji


def main():
    input_str = input("Input: ")
    print(f"Output: {emoji.emojize(input_str, language='alias')}")


if __name__ == "__main__":
    main()
