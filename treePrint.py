#using for loop: Tree printer
def main():
    n = int(input("Enter the tree size: "))
    c = 0
    for i in range(1, n+1):
        print(" " * (n - i), end = "") #first part
        print("^" * i, end = "") #second part gets pushed 
        print("^" * c) #third part sticks
        c += 1
    
if __name__ == "__main__":
    main()