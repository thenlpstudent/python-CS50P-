def main():
    print(format_value(value(input("Greeting: "))))


def value(greeting, desired_greeting="hello"):
    if greeting is None:
        raise ValueError("greeting cannot be none!")
    if len(greeting) == 0:
        raise ValueError("greeting cannot be an empty string!")

    greeting = greeting.strip()
    if greeting.lower()[0] == desired_greeting[0]:
        if len(greeting) < len(desired_greeting):
            return 20
        else:
            if greeting.lower()[0:len(desired_greeting)] == desired_greeting:
                return 0

    return 100


def format_value(val):
    return f"${val}"


if __name__ == "__main__":
    main()
