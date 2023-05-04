def main():
    log = initLog(5)
    log = logRunner(log, addTwo)
    log = logRunner(log, square)
    log = logRunner(log, divideBy5)

    print(log)


def square(n):
    return {
        "result": n ** 2,
        "log": [f"Squaring {n} gives {n ** 2}"]
    }


def addTwo(n):
    return {
        "result": n + 2,
        "log": [f"Adding Two to {n} gives {n + 2}"]
    }


def divideBy5(n):
    return {
        "result": n / 5,
        "log": [f"Dividing {n} by 5 gives {n / 5}"]
    }


def initLog(n):
    return {
        "result": n,
        "log": []
    }


def logRunner(log, func):
    newLog = func(log["result"])
    return {
        "result": newLog["result"],
        "log": log["log"] + newLog["log"]
    }


if __name__ == "__main__":
    main()
