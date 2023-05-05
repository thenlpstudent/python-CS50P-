import string

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date_input = input()
        parsed_date = None
        try:
            if is_date_anno_domini(date_input):
                parsed_date = parse_anno_domini_date(date_input)

            elif is_date_long_format(date_input):
                parsed_date = parse_long_format_date(date_input)

        except ValueError:
            continue

        else:
            if parsed_date:
                print(parsed_date)
                break


def is_date_anno_domini(date):
    try:
        return date[0] in string.digits
    except IndexError:
        return False


def is_valid_date(num):
    return 1 <= num <= 31


def is_valid_month(num):
    return 0 <= num <= len(MONTHS)


def parse_anno_domini_date(date):
    try:
        month, day, year = date.split("/")

        if not is_valid_date(int(day)):
            raise ValueError

        if not is_valid_month(int(month)):
            raise ValueError

    except ValueError:
        raise ValueError("Invalid anno-domino date")

    else:
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"


def is_date_long_format(date):
    try:
        return date.lower()[0] in string.ascii_lowercase
    except IndexError:
        return False


def parse_long_format_date(date):
    try:
        month, day, year = date.split(" ")

        if month not in MONTHS:
            raise ValueError

        month_ind = MONTHS.index(month) + 1
        day = day[:-1]

        if not is_valid_date(int(day)):
            raise ValueError

        return f"{year}-{str(month_ind).zfill(2)}-{day.zfill(2)}"

    except ValueError:
        raise ValueError("Invalid long date format")


if __name__ == "__main__":
    main()
