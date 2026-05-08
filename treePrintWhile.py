#using while loop: Tree Printer
def main():
    n = int(input("Enter the tree size: "))
    size = 1
    c = 0
    while size < n:
        print("0" * (n - 1 - size), end="")
        print("^" * size, end="")
        print("^" * c)
        c += 1
        size += 1

if __name__ == "__main__":
    main()    