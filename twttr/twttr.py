
def main():
    print(shorten(input()))


def shorten(word, skip_letters=["a", "e", "i", "o", "u"]):
    shorten_word = ""

    if word is None:
        raise ValueError("Parameter word cannot be null!")

    for letter in word:
        if letter.lower() in skip_letters:
            continue
        shorten_word += letter

    return shorten_word


if __name__ == "__main__":
    main()
