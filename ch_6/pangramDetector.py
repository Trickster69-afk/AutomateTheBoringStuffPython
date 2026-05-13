#every letter of the alphabet shall appear atleast once
def main():
    str = input("Enter a sentence: ")
    if pangram(str):
        print("The sentence is a pangram")
    else:
        print("The sentence is not a pangram")

def pangram(s):
    letters = []
    pun = [",", "?", ".", "/", "!", ";", "&", ":", "\"", "'", " "]

    for p in pun:
        s = s.replace(p, "").strip().lower() #remove common punctuations and whitespace

    for i in s:
        if i not in letters:
            letters.append(i)
    l = len(letters)
    if l == 26:
        return True
    return False   
        
if __name__ == "__main__":
    main()