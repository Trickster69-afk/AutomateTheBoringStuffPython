#Christmas Tree Printer
import random

def main():
    n = int(input("Enter the tree size: "))
    c = 0
    for i in range(1, n + 1): #First half
        print(" " * (n - i), end = "")
        for j in range(i):
            if random.randint(1,6) == 1:
                print("o", end="")
            else:
                print("^", end="")
                
        for k in range(i - 1): #second half
            if random.randint(1,6) == 1:
                print("o", end="")
            else:
                print("^", end="")
        print()

if __name__ == "__main__":
    main()