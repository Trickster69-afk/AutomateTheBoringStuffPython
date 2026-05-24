def main():
    text = input("Enter a sentence: ")
    spongecase(text)

def spongecase(text):
    text = text.lower()
    result = text[0]
    for i in range(1, len(text)):
        if i%2 != 0:
            result += text[i].upper()
        else:
            result += text[i]
    print(result)
        
if __name__ == "__main__":
    main()
