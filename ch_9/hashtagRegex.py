import re
def main():
    hash = get_hashtags(input("Enter a sentence: "))
    print(hash)

def get_hashtags(s):
    res = re.findall(r"\#\w*", s, re.IGNORECASE)
    return res

if __name__ == "__main__":
    main()