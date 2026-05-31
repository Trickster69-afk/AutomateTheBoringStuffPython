import re
def main():
    price = get_price(input("Enter a sentence: "))
    print(price)

def get_price(s):
    res = re.findall(r"\$\d+\.?\d+", s, re.IGNORECASE)
    return res

if __name__ == "__main__":
    main()