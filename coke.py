ACCEPTED_DEM = [5, 10, 25]
COKE_PRICE = 50

def main():
    n = 0
    while n < COKE_PRICE:
        amount = int(input("Insert Coin: "))
        if (amount not in ACCEPTED_DEM):
            continue
        n += amount
        amount_due = COKE_PRICE - n
        if (amount_due <= 0):
            break
        print("Amount Due: ", amount_due)
    if (amount_due == 0):
        print("Paid in full!")
    else:
        amount_due *= -1
        print("Change owed: ", amount_due)

main()