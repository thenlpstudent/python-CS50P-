def main():
    var_name = input("camelCase: ")
    output_str = ""
    for index, c in enumerate(var_name):
        if (isUpperCaseChar(c)):
            embedChar = "_" + c.lower()
        else:
            embedChar = c
        output_str += embedChar
    print("snake_case : ", output_str)


def isUpperCaseChar(c):
    return c.upper() == c

main()