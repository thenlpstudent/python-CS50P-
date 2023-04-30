VOWELS = ["A", "E", "I", "O", "U"]
def main():
    tweet = input("Input: ")
    print(toTweet(tweet))

def toTweet(tweet):
    transformedTweet = ""
    for ch in tweet:
        if ch.lower() in VOWELS or ch.upper() in VOWELS:
            continue
        transformedTweet += ch
    return transformedTweet

main()