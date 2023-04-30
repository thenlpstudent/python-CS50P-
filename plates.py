import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    for index, ch in enumerate(s):
        if (index == 0 or index == 1):
            if ch not in string.ascii_uppercase:
                return False
        if ch in string.punctuation or ch in [".", " "]:
            return False

        isNumber = ch in string.digits

        if isNumber:
            if ch in string.ascii_uppercase:
                return False
            if ch == "0":
                return False



    return True

main()
